import abc
import character

class Decorator(character.Character, abc.ABC):
    '''An abstract class that extends from Character. It overrides the
    three abstract methods and calls each one on the character attribute.'''

    def __init__(self, c):
        self._char = c

    def description(self):
        return self._char.description()

    def magic_resistance(self):
        return self._char.magic_resistance()

    def strength(self):
        return self._char.strength()
