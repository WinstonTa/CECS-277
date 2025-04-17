import entity
import random

class BegGoblin(entity.Entity):
    def __init__(self):
        self._name = "Goblin"
        self._hp = random.randint(7, 9)
    
    def melee_attack(self, enemy) -> str:
        d = random.randint(4, 6)
        enemy.take_damage(d)
        return f"{self._name} did a ranged attack on {enemy._name} for {d} damage!"
    