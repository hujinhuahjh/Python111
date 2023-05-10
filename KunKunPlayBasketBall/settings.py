class Settings:
    # 存储游戏中所有设置的类
    
    def __init__(self):
        # 初始化游戏设置
        self.screen_width = 1200
        self.screen_height = 680
        self.bg_color = (230, 230, 230)
        self.grade = 1
        
        # 坤坤
        # self.kun_speed = 1.5
        self.kun_limit = 3
        
        # 子弹
        # self.bullet_speed = 1
        # self.bullet_width = 3
        # self.bullet_height = 15
        # self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # 鸡
        # self.ji_speed = 0.25
        self.fleet_drop_speed = 100
        # self.fleet_direction = 1
        
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        self.speed_init = 1
        self.initialize_dynamic_settings()
    
    # 重置游戏设置
    def initialize_dynamic_settings(self):
        if self.speed_init > 1:
            self.kun_speed = 1.5 * self.speed_init / 1.5
            self.bullet_speed = 1.2 * self.speed_init / 1.5
        else:  
            self.kun_speed = 1.5 * self.speed_init
            self.bullet_speed = 1.2 * self.speed_init
            
        self.ji_speed = 0.25 * self.speed_init
        self.speedup_scale *= self.speed_init
        self.score_scale *= self.speed_init
        
        # 记分
        self.ji_points = 50 * self.speed_init
        
        
    # 游戏节奏的速度控制
    def increase_speed(self):
        self.kun_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ji_speed *= self.speedup_scale
        
        self.ji_points = int(self.ji_points * self.score_scale)
        