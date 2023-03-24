import pygame
from pygame.sprite import Sprite

class Ji(Sprite):
    """表示单个鸡的类"""
    
    def __init__(self, ji_game):
        """初始化鸡并设置其起始位置"""
        super().__init__()
        self.screen = ji_game.screen
        self.settings = ji_game.settings
        
        # 加载鸡的图像并设置其rect属性
        self.image = pygame.image.load('KunKunPlayBasketBall/images/ji.png')
        self.image = pygame.transform.smoothscale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        
        # 每只最初鸡都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 存储鸡的精确水平位置
        self.x = float(self.rect.x)
        
    def update(self):
        self.x += (self.settings.ji_speed * self.settings.fleet_direction)
        self.rect.x = self.x
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        