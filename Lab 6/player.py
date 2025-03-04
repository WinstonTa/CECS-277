import die

class Player():
    def __init__(self):
        self._dice = [die.Die(), die.Die(), die.Die()]
        self._points = 0

    def points(self):
        return self._points
    
    def roll_dice(self):
        die1 = self._dice[0].roll()
        die2 = self._dice[1].roll()
        die3 = self._dice[2].roll()

        self._dice = [die1, die2, die3]
        self._dice.sort()


    def has_pair(self):
        if self._dice[0] == self._dice[1] or self._dice[1] == self._dice[2] \
        or self._dice[0] == self._dice[2]:
            self.points += 1
            return True
        
    def has_three_of_a_kind(self):
        if self.dice[0] == self._dice[1] and self._dice[1] == self._dice[2]:
            self.points += 3
            return True
        
    def has_series(self):
        pass

    def __str__(self):
        return f"D1={self._dice[0]} D2={self._dice[1]} D3={self._dice[2]}"
