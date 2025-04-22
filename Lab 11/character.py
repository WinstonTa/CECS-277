import abc

class Character(abc.ABC):
    @abc.abstractmethod
    def description(self):
        # character's name and items
        pass

    @abc.abstractmethod
    def magic_resistance(self):
        # character's magic resist value
        pass

    @abc.abstractmethod
    def strength(self):
        # character's strength valu
        pass

    @abc.abstractmethod
    def __str__(self):
        # returns character's description, magic resistance, and strength
        pass
