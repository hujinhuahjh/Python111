import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # 管理坤坤打出篮球的类
    
    def __init__(self, ji_game):
        # 在坤坤当前位置射出一个篮球对象
        super().__init__()
        self.screen = ji_game.screen
        self.settings = ji_game.settings
        # self.color = self.settings.bullet_color
        
        # 在(0,0)处创建一个表示子弹的矩形
        # self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # self.rect.midtop = ji_game.kun.rect.midtop
        
        # 加载篮球图像
        self.image = pygame.image.load('KunKunPlayBasketBall/images/basketball.png')
        self.image = pygame.transform.smoothscale(self.image, (25,25))
        self.rect = self.image.get_rect()
        self.rect.midtop = ji_game.kun.rect.midtop
        
        self.y = float(self.rect.y)
        
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        # 在屏幕上绘制篮球
        # pygame.draw.rect(self.screen, self.color, self.rect)
        # 在屏幕上加载篮球
        self.screen.blit(self.image, self.rect)
        