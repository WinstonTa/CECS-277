import abc
import character

class Decorator(character.Character, abc.ABC):
    def __init__(self, char):
        self._character = char

    def description(self):
        return self._character.description()

    def magic_resistance(self):
        return self._character.magic_resistance()

    def strength(self):
        return self._character.strength()
