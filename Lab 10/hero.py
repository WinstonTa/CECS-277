import entity
import random

class Hero(entity.Entity):
    def __init__(self, name):
        self._name = name
        self._hp = 30
    
    def melee_attack(self, enemy: entity) -> str:
        """
        A certain entity conducts a melee attack upon another entity, and details out the process.

        Args:
            enemy (entity): The target of the melee attack.

        Returns:
            A string detailing the details of the melee attack.
        """

        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        enemy.take_damage(d1 + d2)
        return f"{self._name} did a melee attack on {enemy._name} for {d1 + d2} damage!"
    
    def ranged_attack(self, enemy: entity) -> str:
        """
        A certain entity conducts a ranged attack upon another entity, and details out the process.

        Args:
            enemy (entity): The target of the ranged attack.

        Returns:
            A string detailing the details of the ranged attack.
        """

        d = random.randint(1, 12)
        enemy.take_damage(d)
        return f"{self._name} did a ranged attack on {enemy._name} for {d} damage!"
    