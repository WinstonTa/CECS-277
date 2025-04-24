import abc

class Character(abc.ABC): 
    '''Interface, sets groundwork for other classes.'''

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

    def __str__(self):
        # returns character's description, magic resistance, and strength
        return f"Name: {self.description()}\nMR: {self.magic_resistance()}\nStrength: {self.strength()}"
