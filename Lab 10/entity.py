import abc

class Entity(abc.ABC):
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def hp(self) -> float:
        return self._hp
    
    def take_damage(self, dmg):
        # entity will only take damage if its hp does not drop below 0
        # entity will otherwise have 0 hp
        if self._hp - dmg >= 0:
            self._hp -= dmg
        else:
            self._hp = 0
    
    def __str__(self):
        return f"{self._name} HP: {self._hp}"
    
    @abc.abstractmethod
    def melee_attack(self, enemy):
        pass
    