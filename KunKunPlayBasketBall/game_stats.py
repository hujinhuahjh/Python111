class GameStats:
    def __init__(self, ji_game):
        self.settings = ji_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        
    def reset_stats(self):
        self.kuns_left = self.settings.kun_limit
        self.score = 0
        self.level = 1