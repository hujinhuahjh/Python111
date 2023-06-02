import pygame.font
from pygame.sprite import Group
from kun import Kun

class Scoreboard:
    # 显示得分信息的类
    
    def __init__(self, ji_game):
        # 初始化涉及得分的属性
        self.ji_game = ji_game
        self.screen = ji_game.screen
        self.screen_rect = ji_game.screen.get_rect()
        self.settings = ji_game.settings
        self.stats = ji_game.stats
        
        # 字体
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # 准备图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_kuns()
    
    # 右上角显示得分
    def prep_score(self):
        # 将得分渲染成图像
        # score_str = str(self.stats.score)
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, 
                                            self.settings.bg_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    # 屏幕底部中央显示最高分
    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, 
                                                 self.text_color, self.settings.bg_color)
        
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    # 检查最高分是否变化  
    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    # 将最高得分转换为渲染的图像
    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = 'High_Score: ' + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                                 self.settings.bg_color)

        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    # 显示当前游戏关卡等级
    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, 
                                            self.settings.bg_color)
        
        self.level_rect = self.score_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    
    # 屏幕左上角显示剩余生命值
    def prep_kuns(self):
        self.kuns = Group()
        for kun_number in range(self.stats.kuns_left):
            kun = Kun(self.ji_game)
            kun.image = pygame.transform.smoothscale(kun.image, (33, 50))
            kun.rect.x = kun_number * kun.rect.width
            kun.rect.y = 5
            self.kuns.add(kun)
    
    # 显示在屏幕上
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.kuns.draw(self.screen)