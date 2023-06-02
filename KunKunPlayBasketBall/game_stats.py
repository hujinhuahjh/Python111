class GameStats:
    # 跟踪游戏的统计信息
    
    def __init__(self, ji_game):
        # 初始化统计信息
        self.settings = ji_game.settings
        self.reset_stats()
        # 游戏处于非活动状态
        self.game_active = False
        self.high_score = self.load_high_score()
        
    def reset_stats(self):
        # 初始化游戏运行期间可能变化的统计信息
        self.kuns_left = self.settings.kun_limit
        self.score = 0
        self.level = 1
        
    def save_high_score(self):
        """保存最高得分"""
        with open('score.txt', 'w') as file_object:
            file_object.write(str(self.high_score))
            file_object.close()

    def load_high_score(self):
        """加载最高得分"""
        try:
            with open('score.txt') as file_object:
                h_s = file_object.read()
                try:
                    self.high_score = int(h_s)
                except ValueError:
                    self.high_score = 0
                file_object.close()
                return self.high_score
        except FileNotFoundError:
            with open('score.txt', 'w') as file_object:
                file_object.close()