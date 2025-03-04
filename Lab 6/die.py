import random

class Die:
    def __initit__(self, sides: int = 6):
        self._sides = sides
        self._value = 0

    def roll(self) -> int:
        self._value = random.randint(1, self._sides)
        return self._value

    def __str__(self) -> str:
        return str(self._value)

    def __lt__(self, other) -> bool:
        if self._value < other:
            return True

    def __eq__(self, other) -> bool:
        if self._value == other:
            return True

    def __sub__(self, other) -> int:
        return self._value - other
