import entity
import random

class ExpTroll(entity.Entity):
    def __init__(self):
        self._name = "Tyrannical Troll"
        self._hp = random.randint(15, 18)
    
    def melee_attack(self, enemy) -> str:
        d = random.randint(8, 12)
        enemy.take_damage(d)
        return f"{self._name} did a ranged attack on {enemy._name} for {d} damage!"
    