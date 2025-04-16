import entity
import random

class BegTroll(entity.Entity):
    def __init__(self):
        self._name = "Troll"
        self._hp = random.randint(8, 10)
    
    def melee_attack(self, enemy) -> str:
        d = random.randint(5, 9)
        enemy.take_damage(d)
        return f"{self._name} did a ranged attack on {enemy} for {d} damage!"
    