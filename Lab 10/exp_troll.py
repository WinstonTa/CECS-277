import entity
import random

class ExpTroll(entity.Entity):
    def __init__(self):
        self._name = "Angry Troll"
        self._hp = random.randint(15, 18)
    
    def melee_attack(self, enemy) -> str:
        d = random.randint(8, 12)
        enemy.take_damage(d)
        return f"{self._name} did a ranged attack on {enemy} for {d} damage!"
    