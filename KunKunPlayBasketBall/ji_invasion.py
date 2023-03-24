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
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.background = pygame.image.load('KunKunPlayBasketBall/images/lianxisheng.png')  
        
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("鸡你太美")
        
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        self.kun = Kun(self)
        self.bullets = pygame.sprite.Group()
        self.jis = pygame.sprite.Group()
        
        self._create_fleet()
        self.play_button = Button(self, "play")
        
    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.kun.update()
                self._update_bullets()
                self._update_jis()
                
            self._update_screen()
    
    # 响应按键与鼠标事件      
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.kun.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.kun.moving_left = False
        elif event.key == pygame.K_UP:
            self.kun.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.kun.moving_bottom = False
    
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_kuns()
            self.jis.empty()
            self.bullets.empty()
            sleep(1)
            
            self._create_fleet()
            self.kun.center_kun()
            sleep(1)
            
            pygame.mouse.set_visible(False)
    
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        self.bullets.update();
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
        # collisions = pygame.sprite.groupcollide(self.bullets, self.jis, True, True)
        # if not self.jis:
        #     self.bullets.empty()
        #     self._create_fleet()
        self._check_bullet_ji_collisions()
            
    def _check_bullet_ji_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.jis, True, True)
        if collisions:
            for jis in collisions.values():
                self.stats.score += self.settings.ji_points * len(jis)
                self.sb.prep_score()
                self.sb.check_high_score()
        if not self.jis:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
        
    def _create_fleet(self):
        ji = Ji(self)
        ji_width, ji_height = ji.rect.size
        available_space_x = self.settings.screen_width - (2 * ji_width)
        number_jis_x = available_space_x // (2 * ji_width)
        
        kun_height = self.kun.rect.height
        available_space_y = (self.settings.screen_height - (3 * ji_height) - kun_height - 100)
        number_rows = available_space_y // (2 * ji_height)
        
        for row_number in range(number_rows):
            for ji_number in range(number_jis_x):
                self._create_ji(ji_number, row_number)
            
    def _create_ji(self, ji_number, row_number):
        ji = Ji(self)
        ji_width, ji_height = ji.rect.size
        ji.x = ji_width + 2 * ji_width * ji_number
        ji.rect.x = ji.x
        ji.rect.y = ji.rect.height + 2 * ji.rect.height * row_number
        self.jis.add(ji)
    
    def _check_fleet_edges(self):
        for ji in self.jis.sprites():
            if ji.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        for ji in self.jis.sprites():
            ji.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
    def _check_jis_bottom(self):
        screen_rect = self.screen.get_rect()
        for ji in self.jis.sprites():
            if ji.rect.bottom > screen_rect.bottom:
                self._kun_hit()
                break
    
    def _update_jis(self):
        self._check_fleet_edges()
        self.jis.update()
        if pygame.sprite.spritecollideany(self.kun, self.jis):
            sleep(1)
            self._kun_hit()
        self._check_jis_bottom()
            
    def _kun_hit(self):
        if self.stats.kuns_left > 0:
            self.stats.kuns_left -= 1
            self.sb.prep_kuns()
            
            sleep(1)
            self.jis.empty()
            self.bullets.empty()
            sleep(1)
            
            self._create_fleet()
            self.kun.center_kun()
            sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
        
    # 更新屏幕图像
    def _update_screen(self):
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.background, (0, 0))
        self.kun.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.jis.draw(self.screen)
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        # pygame.display.update()
        pygame.display.flip()
        
            
if __name__ == "__main__":
    ji = JiInvasion()
    ji.run_game()
    
