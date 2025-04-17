import abc

class Entity(abc.ABC):
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp
    
    @property
    def name(self) -> str:
        """returns the name of the entity"""
        return self._name
    
    @property
    def hp(self) -> int:
        """returns the hp value of the entity"""
        return self._hp
    
    def take_damage(self, dmg: int):
        """
        Causes the affected entity to take the desired amount of damage passed into dmg.

        Args:
            dmg (int): A damage value as an integer.
        """

        # entity will only take damage if its hp does not drop below 0
        # entity will otherwise have 0 hp
        if self._hp - dmg >= 0:
            self._hp -= dmg
        else:
            self._hp = 0
    
    def __str__(self):
        """returns information about the entity, its name, and its remaining hp"""
        return f"{self._name} HP: {self._hp}"
    
    @abc.abstractmethod
    def melee_attack(self, enemy):
        """abstract method of melee_attack, to be implemented by other classes"""
        pass
