import dragon
import random

class FlyingDragon(dragon.Dragon()):

    def __init__(self, name, hp):
        """Initialize FlyingDragon"""
        super().__init__(name, hp)
        self._swoops = 3

    def special_attack(self, hero) -> str:
        """
        FlyingDragon inflicts special swoop attack.

        Args:
            hero (entity): the hero (passed in as an entity) that will be hurt through swoop attack
        
        Returns:
            A string describing the swoop attack.
        """
        # swoop attack does random damage from 5-8 hp
        d = random.randint(5, 8)

        # FlyingDragon only attacks with more than 0 swwops
        if self._swoops > 0:
            self._swoops -= 1
            hero.take_damage(d)

            return f"{self.name} swoops you with their majestic grace for {d} damage!"
        else:
            # fail message if no swoops remain
            return f"{self.name} tried to fly up and majestically destroy you, but ran out of energy before attacking!"

    def __str__(self):
        # string inherits from Dragon and adds swoop count left
        super().__str__() + f"\nSwoop Attacks Remaining: {self._swoops}"
