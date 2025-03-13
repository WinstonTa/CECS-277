import dragon
import random

class FireDragon(dragon.Dragon()):

    def __init__(self, name, hp):
        super().__init__(name, hp)
        self._fire_shots = 3

    def special_attack(self, hero):
        if self._fire_shots > 0:
            d = random.randint(6,9)
            self._fire_shots -= 1
            return f'{self.name} engulfs you in falmes for {d} damage!'  
        else:
            return f'{self.name} tries to spit fire at you but is all out of fire shots.'  

    def __str__(self):
        super().__str__() + f'\nFire Shots remaining: {self._fire_shots}'