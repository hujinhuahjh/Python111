import pygame
from pygame.sprite import Sprite

class Kun(Sprite):
    # 管理坤坤的类
    
    def __init__(self, ji_game):
        # 初始化坤坤并设置其初始位置
        super().__init__()
        self.screen = ji_game.screen
        self.settings = ji_game.settings
        self.screen_rect = ji_game.screen.get_rect()
        
        # 加载坤坤图像并获取外接矩形
        self.image = pygame.image.load('KunKunPlayBasketBall/images/kunkun.png')
        self.image = pygame.transform.smoothscale(self.image, (66, 100))
        self.rect = self.image.get_rect()
        # 最初位置位于屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        # 存储飞船属性，移动标志
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False
    
    #  根据移动标志调整坤坤位置    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.kun_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.kun_speed
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.kun_speed
        if self.moving_top and self.rect.top > 0:
            self.y -= self.settings.kun_speed
            
        self.rect.x = self.x
        self.rect.y = self.y
        
            
    def blitme(self):
        # 在指定位置绘制坤坤
        self.screen.blit(self.image, self.rect)
        
    def center_kun(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)