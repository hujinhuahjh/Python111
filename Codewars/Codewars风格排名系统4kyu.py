# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method

class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
        
    def inc_progress(self, topic_rank):
        if topic_rank > 8 or topic_rank < -8 or topic_rank == 0:
            raise ValueError
        if self.rank > topic_rank and self.rank - topic_rank <= 2:
                self.progress += 1
        elif self.rank > topic_rank and self.rank - topic_rank > 2:
            self.progress += 1
        elif self.rank == topic_rank:
            self.progress += 3
        else:
            if self.rank < 0 and topic_rank > 0:
                self.progress += ((topic_rank - self.rank - 1) ** 2) * 10
            else:
                self.progress += ((topic_rank - self.rank) ** 2) * 10
        print(topic_rank - self.rank)
        self.progress_change()
        
    def progress_change(self):
        if self.progress >= 100:
            flag = False
            if self.rank < 0:
                flag = True
            self.rank += int(self.progress / 100)
            if self.rank >=0 and flag:
                self.rank += 1
            self.progress %= 100
            
user = User()
user.inc_progress(10)
print(user.progress)
print(user.rank)