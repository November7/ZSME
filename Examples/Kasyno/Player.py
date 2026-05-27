class Player:
    def __init__(self, name):
        self.name = name
        self.__score = 10


    def lvl(self):
        gap = 10
        score = self.__score
        gap_vel = 1.5
        clvl = 1
        while score > gap:
            score -= gap
            clvl += 1
            gap *= gap_vel
        return clvl
    
    def __str__(self):
        return f"{self.name}, {self.lvl()} LVL, {self.__score} points"

    @property
    def score(self):            
        return self.__score
    
    @score.setter
    def score(self, value):                
        self.__score = value
        if self.__score < 0:
            raise ValueError("Player lost all points! Game over.")
