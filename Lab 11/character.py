import abc

class Character(abc.ABC):
    def description(self):
        # character's name and items
        pass

    def magic_resistance(self):
        # character's magic resist value
        pass

    def strength(self):
        # character's strength valu
        pass

    def __str__(self):
        # returns character's description, magic resistance, and strength
        pass
