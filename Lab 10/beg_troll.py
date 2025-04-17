import entity
import random

class BegTroll(entity.Entity):
    def __init__(self):
        self._name = "Troll"
        self._hp = random.randint(8, 10)
    
    def melee_attack(self, enemy: entity) -> str:
        """
        A beginner troll conducts a melee attack upon the hero, an entity, and details out the process.

        Args:
            enemy (entity): The target of the melee attack.

        Returns:
            A string detailing the details of the melee attack.
        """
        d = random.randint(5, 9)
        enemy.take_damage(d)
        return f"{self._name} did a ranged attack on {enemy._name} for {d} damage!"
    