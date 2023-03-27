class GameStats:
    # 跟踪游戏的统计信息
    
    def __init__(self, ji_game):
        # 初始化统计信息
        self.settings = ji_game.settings
        self.reset_stats()
        # 游戏处于非活动状态
        self.game_active = False
        self.high_score = 0
        
    def reset_stats(self):
        # 吃石化游戏运行期间可能变化的统计信息
        self.kuns_left = self.settings.kun_limit
        self.score = 0
        self.level = 1