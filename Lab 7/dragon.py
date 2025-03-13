import entity
import random

class Dragon(entity.Entity()):
    
    def basic_attack(self, hero: entity) -> str:
        """
        Dragon inflicts basic tail attack.

        Args:
            hero (entity): the hero (passed in as an entity) that will be hurt through tail attack
        
        Returns:
            A string describing the tail attack.
        """
        
        # tail attack does random damage from 2-5 hp
        d = random.randint(2, 5)
        hero.take_damage(d)

        return f"{self.name} smashes you with their tail for {d} damage!"

    def special_attack(self, hero: entity) -> str:
        """
        Dragon inflicts special claw attack.

        Args:
            hero (entity): the hero (passed in as an entity) that will be hurt through claw attack
        
        Returns:
            A string describing the claw attack.
        """
        # claw attack does random damage from 3-7 hp
        d = random.randint(3, 7)
        hero.take_damage(d)

        return f"{self.name} slashes you with their claws for {d} damage!"
