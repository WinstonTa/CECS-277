import random

class Die:
    '''passes in the number of sides of the die. Assign sides
        using the parameter and set value to either 0 or to the returned value of roll()'''
    def __init__(self, sides: int = 6):
        self._sides = sides
        self._value = 0

    '''generate a random number between 1 and the number of sides and assign it to value and return it'''
    def roll(self) -> int:
        self._value = random.randint(1, self._sides)
        return self._value

    '''return the Die's value as a string'''
    def __str__(self) -> str:
        return str(self._value)

    '''return true if the value of self is less than the value of the other'''
    def __lt__(self, other) -> bool:
        if self._value < other:
            return True

    '''return true if the value of self is equal to the value of other'''
    def __eq__(self, other) -> bool:
        if self._value == other:
            return True

    '''return the difference ebtween the value of self and the value of other'''
    def __sub__(self, other) -> int:
        return self._value - other
