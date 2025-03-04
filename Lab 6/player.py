import die

class Player():
    def __init__(self):
        self.dice = [die.Die(), die.Die(), die.Die()]
        self._points = 0

    def points(self):
        return self._points
    
    def roll_dice(self):
        die1 = self.dice[0].roll()
        die2 = self.dice[1].roll()
        die3 = self.dice[2].roll()

        pass



    def has_pair(self):
        if self.dice[0] == self.dice[1] or self.dice[1] == self.dice[2] \
        or self.dice[0] == self.dice[2]:
            self.points += 1
            return True
        
    def has_three_of_a_kind(self):
        if self.dice[0] == self.dice[1] and self.dice[1] == self.dice[2]:
            self.points += 3:
            return True
        
    def has_series(self):
        pass

    def __str__(self):
        return f"D1={self.dice[0]} D2={self.dice[1]} D3={self.dice[2]}"
