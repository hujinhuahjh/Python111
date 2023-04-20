class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
        
    def inc_progress(self, activity_rank):
        if activity_rank not in range(-8, 0) and activity_rank not in range(1, 9):
            raise ValueError("Invalid rank value")
        
        rank_diff = activity_rank - self.rank
        
        if rank_diff == 0:
            progress = 3
        elif rank_diff == -1 or (activity_rank == -1 and self.rank == 1):
            progress = 1
        elif rank_diff >= 1:
            if activity_rank * self.rank <= 0:
                progress = ((activity_rank - self.rank - 1) ** 2) * 10
            else:
                progress = ((activity_rank - self.rank) ** 2) * 10
        else:
            progress = 0
        
        self.progress += progress
        
        pre_rank = self.rank
        while self.progress >= 100 and self.rank < 8:
            self.progress -= 100
            self.rank += 1
        if self.rank * pre_rank <= 0:
            self.rank += 1
            
        if self.rank >= 8:
            self.rank = 8
            self.progress = 0
            
user = User()
user.inc_progress(5)
print(user.progress)
print(user.rank)