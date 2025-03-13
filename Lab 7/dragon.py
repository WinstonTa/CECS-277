import entity
import random

class Dragon(entity.Entity()):
    
    def basic_attack(self, hero):
        d = random.randint(2, 5)
        hero.take_damage(d)

        return f"{self.name} smashes you with their tail for {d} damage!"

    def special_attack(self, hero):
        d = random.randint(3, 7)
        hero.take_damage(d)

        return f"{self.name} slashes you with their claws for {d} damage!"
