import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self, ji_game):
        super().__init__()
        self.screen = ji_game.screen
        self.settings = ji_game.settings
        # self.color = self.settings.bullet_color
        
        # self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # self.rect.midtop = ji_game.kun.rect.midtop
        self.image = pygame.image.load('KunKunPlayBasketBall/images/basketball.png')
        self.image = pygame.transform.smoothscale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.midtop = ji_game.kun.rect.midtop
        
        self.y = float(self.rect.y)
        
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)
        