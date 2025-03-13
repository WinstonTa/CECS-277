import dragon
import random

class FireDragon(dragon.Dragon()):

    def __init__(self, name, hp):
        """Initializes FireDragon"""
        super().__init__(name, hp)
        self._fire_shots = 3

    def special_attack(self, hero) -> str:
        """
        FireDragon inflicts special flame attack.

        Args:
            hero (entity): the hero (passed in as an entity) that will be hurt through flame attack

        Returns:
            A string describing the flame attack.
        """

        # will only fire shots if shots are greater than 0
        if self._fire_shots > 0:
            # random damage from 6-9 hp
            d = random.randint(6, 9)
            hero.take_damage(d)
            self._fire_shots -= 1
            return f'{self.name} engulfs you in flames for {d} damage!'  
        else:
            # fail message if no shots left
            return f'{self.name} tries to spit fire at you but is all out of fire shots.'  

    def __str__(self):
        # inherits from entity the string representation and adds fire shots left
        super().__str__() + f'\nFire Shots remaining: {self._fire_shots}'
