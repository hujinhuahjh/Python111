import pygame.font

class Button:
    def __init__(self, ji_game, msg):
        # 初始化按钮属性
        self.screen = ji_game.screen
        self.screen_rect = ji_game.screen.get_rect()
        
        # 按钮尺寸
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # 按钮标签
        self._prep_msg(msg)
     
        
    # 将msg渲染成图像并居中
    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    # 绘制按钮
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)