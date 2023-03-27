import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from kun import Kun
from bullet import Bullet
from ji import Ji
from button import Button
from scoreboard import Scoreboard

class JiInvasion:
    # 管理游戏资源和行为的类 
    
    def __init__(self):
    # 初始化游戏并创建游戏资源
        pygame.init()
        self.settings = Settings()
        #绘制游戏窗口
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # 设置游戏背景
        self.background = pygame.image.load('KunKunPlayBasketBall/images/lianxisheng.png')  
        
        # 全屏运行
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("鸡你太美")
        
        # 创建存储游戏信息的实例
        self.stats = GameStats(self)
        
        # 创建记分牌
        self.sb = Scoreboard(self)
        
        self.kun = Kun(self)
        # 存储篮球及鸡群的编组
        self.bullets = pygame.sprite.Group()
        self.jis = pygame.sprite.Group()
        
        self._create_fleet()
        self.play_button = Button(self, "Music")
        
    def run_game(self):
        # 开始游戏主循环
        while True:
            # 监控键盘和鼠标事件
            self._check_events()
            
            # 如果游戏状态被改变（点击play按钮或游戏结束）
            if self.stats.game_active:
                # 更新坤坤图像
                self.kun.update()
                # 更新子弹图像
                self._update_bullets()
                # 更新鸡图像
                self._update_jis()
                
            # 更新游戏图像
            self._update_screen()
    
    # 响应按键与鼠标事件      
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 开始游戏
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    # 响应按键
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.kun.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.kun.moving_left = True
        elif event.key == pygame.K_UP:
            self.kun.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.kun.moving_bottom = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        # 发射篮球
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    # 响应松开
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.kun.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.kun.moving_left = False
        elif event.key == pygame.K_UP:
            self.kun.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.kun.moving_bottom = False
    
    # 响应按下play按钮
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # 重置游戏统计信息
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            
            # 重置得分信息
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_kuns()
            
            # 清空鸡群和篮球
            self.jis.empty()
            self.bullets.empty()
            sleep(1)
            
            self._create_fleet()
            self.kun.center_kun()
            sleep(1)
            
            # 隐藏鼠标
            pygame.mouse.set_visible(False)
    
    
    # 创建一颗篮球，并将其加入到编组bullets当中
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
        
    # 检测篮球和鸡是否发生碰撞
    def _check_bullet_ji_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.jis, True, True)
        if collisions:
            for jis in collisions.values():
                self.stats.score += self.settings.ji_points * len(jis)
                self.sb.prep_score()
                self.sb.check_high_score()
        if not self.jis:
            # 如果鸡群都被消灭了，删除现有子弹，并创建新的鸡群
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
    
        
    # 创建鸡群
    def _create_fleet(self):
        ji = Ji(self)
        # 计算一行可容纳多少个外星人
        ji_width, ji_height = ji.rect.size
        available_space_x = self.settings.screen_width - (2 * ji_width)
        number_jis_x = available_space_x // (2 * ji_width)
        
        # 计算屏幕可容纳多少鸡
        kun_height = self.kun.rect.height
        available_space_y = (self.settings.screen_height - (3 * ji_height) - kun_height - 100)
        number_rows = available_space_y // (2 * ji_height)
        
        for row_number in range(number_rows):
            for ji_number in range(number_jis_x):
                self._create_ji(ji_number, row_number)
    
    
    # 创建一行鸡 
    def _create_ji(self, ji_number, row_number):
        ji = Ji(self)
        ji_width, ji_height = ji.rect.size
        ji.x = ji_width + 2 * ji_width * ji_number
        ji.rect.x = ji.x
        ji.rect.y = ji.rect.height + 2 * ji.rect.height * row_number
        self.jis.add(ji)
    
    
    # 检测鸡群是否位于屏幕边缘
    def _check_fleet_edges(self):
        for ji in self.jis.sprites():
            # 如果是改变其移动方向
            if ji.check_edges():
                self._change_fleet_direction()
                break
    
    
    # 将鸡群下移并改变运动方向
    def _change_fleet_direction(self):
        for ji in self.jis.sprites():
            ji.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    
    # 检测鸡群是否到达了底部
    def _check_jis_bottom(self):
        screen_rect = self.screen.get_rect()
        for ji in self.jis.sprites():
            if ji.rect.bottom >= screen_rect.bottom:
                # 像坤坤被撞到了一样处理
                self._kun_hit()
                break


    # 响应坤坤被鸡群撞到
    def _kun_hit(self):
        if self.stats.kuns_left > 0:
            # 坤坤生命值减1
            self.stats.kuns_left -= 1
            self.sb.prep_kuns()
            
            # 清空鸡群和篮球
            sleep(1)
            self.jis.empty()
            self.bullets.empty()
            sleep(1)
            
            # 创建新的鸡群，并将飞船放到底部
            self._create_fleet()
            self.kun.center_kun()
            sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    
    # 更新所有鸡的位置
    def _update_jis(self):
        self._check_fleet_edges()
        self.jis.update()
        if pygame.sprite.spritecollideany(self.kun, self.jis):
            sleep(1)
            self._kun_hit()
        self._check_jis_bottom()
        
            
    def _update_bullets(self):
        # 更新篮球的位置
        self.bullets.update();
        # 删除消失的篮球
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
        # collisions = pygame.sprite.groupcollide(self.bullets, self.jis, True, True)
        # if not self.jis:
        #     self.bullets.empty()
        #     self._create_fleet()
        self._check_bullet_ji_collisions()
        
    
    # 更新屏幕图像
    def _update_screen(self):
        # self.screen.fill(self.settings.bg_color)
        # 重绘屏幕
        self.screen.blit(self.background, (0, 0))
        self.kun.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.jis.draw(self.screen)
        
        # 显示得分 
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        # pygame.display.update()
        # 让屏幕可见
        pygame.display.flip()
       
        
            
if __name__ == "__main__":
    ji = JiInvasion()
    ji.run_game()
    
