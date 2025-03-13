import dragon
import random

class FlyingDragon(dragon.Dragon()):

    def __init__(self, name, hp):
        super().__init__(name, hp)
        self._swoops = 3

    def special_attack(self, hero):
        d = random.randint(5, 8)
        if self._swoops > 0:
            self._swoops -= 1
            hero.take_damage(d)

            return f"{self.name} swoops you with their majestic grace for {d} damage!"
        else:
            return f"{self.name} tried to fly up and majestically destroy you, but ran out of energy before attacking!"

    def __str__(self):
        super().__str__() + f"\nSwoop Attacks Remaining: {self._swoops}"
