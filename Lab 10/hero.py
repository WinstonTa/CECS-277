import entity
import random

class Hero(entity.Entity):
    def __init__(self, name):
        self._name = name
        self._hp = 30
    
    def melee_attack(self, enemy) -> str:
        d1, d2 = random.randint(1, 6)
        enemy.take_damage(d1 + d2)
        return f"{self._name} did a melee attack on {enemy} for {d1 + d2} damage!"
    
    def ranged_attack(self, enemy) -> str:
        d = random.randint(1, 12)
        enemy.take_damage(d)
        return f"{self._name} did a ranged attack on {enemy} for {d} damage!"
    