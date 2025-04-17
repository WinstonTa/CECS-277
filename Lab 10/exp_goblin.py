import entity
import random

class ExpGoblin(entity.Entity):
    def __init__(self):
        self._name = "Grotesque Goblin"
        self._hp = random.randint(12, 15)
    
    def melee_attack(self, enemy) -> str:
        d = random.randint(5, 8)
        enemy.take_damage(d)
        return f"{self._name} did a ranged attack on {enemy._name} for {d} damage!"
    