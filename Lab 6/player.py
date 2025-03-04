import die

class Player():
    '''constructs and sorts the list of three Die objects and then initializes
        the player’s points to 0'''
    def __init__(self):
        self._dice = [die.Die(), die.Die(), die.Die()]
        self._points = 0

    '''get property that returns the player's points'''
    def points(self):
        return self._points
    
    '''calls roll on each of the Die objects in the list and then sorts the list'''
    def roll_dice(self):
        die1 = self._dice[0].roll()
        die2 = self._dice[1].roll()
        die3 = self._dice[2].roll()

        self._dice = [die1, die2, die3]
        self._dice.sort()

    '''returns true if two dice in the list have the same value, increments points by 1 if true'''
    def has_pair(self):
        if self._dice[0] == self._dice[1] or self._dice[1] == self._dice[2] \
        or self._dice[0] == self._dice[2]:
            self.points += 1
            return True

    '''returns true if all three dice in the list have the same value, increments points by 3 if true'''  
    def has_three_of_a_kind(self):
        if self._dice[0] == self._dice[1] and self._dice[1] == self._dice[2]:
            self.points += 3
            return True

    '''returns true if the value of each dice in the list are in a sequence, increments points by 2 if true'''    
    def has_series(self):
        if (self._dice[2] - self._dice[1]) == 1 and (self._dice[1] - self._dice[0]) == 1:
            self.points += 2
            return True

    '''returns a string in the format: “D1=2, D2=4, D3=6”'''
    def __str__(self):
        return f"D1={self._dice[0]} D2={self._dice[1]} D3={self._dice[2]}"
