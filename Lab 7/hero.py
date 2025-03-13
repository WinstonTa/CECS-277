import entity
import random

class Hero(entity.Entity()):

    def sword_attack(self, dragon):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        total_dmg = d1 + d2
        dragon.take_damage(total_dmg)

        return f"You attacked the {dragon.name} with your sword for {total_dmg} damage."

    def arrow_attack(self, dragon):
        d = random.randint(1, 12)
        dragon.take_damage(d)

        return f"You attacked the {dragon.name} with your bow for {d} damage."
