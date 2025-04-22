import abc
import character

class Decorator(character.Character, abc.ABC):
    def __init__(self, c):
        self._char = c

    def description(self):
        return self._char.description()

    def magic_resistance(self):
        return self._char.magic_resistance()

    def strength(self):
        return self._char.strength()
