import pygame.font

class Button:
    def __init__(self, ji_game, msg):
        # 初始化按钮属性
        self.screen = ji_game.screen
        self.screen_rect = ji_game.screen.get_rect()
        
        # 按钮尺寸
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('华文仿宋', 36)
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # 按钮标签
        self._prep_msg(msg)
        self._prep_grade()
     
        
    # 将msg渲染成图像并居中
    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    # 将关卡等级渲染成图像并居中
    def _prep_grade(self):
        self.grade_image1 = self.font.render("等级1", True, self.text_color, self.button_color)
        self.grade_image1_rect = self.grade_image1.get_rect()
        self.grade_image1_rect.center = self.msg_image_rect.center
        self.grade_image1_rect.top = self.msg_image_rect.bottom + 20
                
        self.grade_image2 = self.font.render("等级2", True, self.text_color, self.button_color)
        self.grade_image2_rect = self.grade_image2.get_rect()
        self.grade_image2_rect.center = self.msg_image_rect.center
        self.grade_image2_rect.top = self.grade_image1_rect.bottom + 20
        
        self.grade_image3 = self.font.render("等级3", True, self.text_color, self.button_color)
        self.grade_image3_rect = self.grade_image3.get_rect()
        self.grade_image3_rect.center = self.msg_image_rect.center
        self.grade_image3_rect.top = self.grade_image2_rect.bottom + 20
    
    # 绘制按钮
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.grade_image1, self.grade_image1_rect)
        self.screen.blit(self.grade_image2, self.grade_image2_rect)
        self.screen.blit(self.grade_image3, self.grade_image3_rect)
        