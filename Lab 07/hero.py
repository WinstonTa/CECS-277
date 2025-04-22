import entity
import random

class Hero(entity.Entity):

    def sword_attack(self, dragon: entity) -> str:
        """
        Hero inflicts sword attack.

        Args:
            dragon (entity): the dragon (passed in as an entity) that will be hurt through sword attack

        Returns:
            A string describing the sword attack.
        """

        # randomizes 2 dice with rolls from 1-6, then totals it, then dragon takes that total damage
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        total_dmg = d1 + d2
        dragon.take_damage(total_dmg)

        return f"You attacked the {dragon.name} with your sword for {total_dmg} damage."

    def arrow_attack(self, dragon: entity) -> str:
        """
        Hero inflicts arrow attack.

        Args:
            dragon (entity): the dragon (passed in as an entity) that will be hurt through arrow attack

        Returns:
            A string describing the arrow attack.
        """

        # randomizes 1 dice with rolls from 1-12, then dragon takes that damage
        d = random.randint(1, 12)
        dragon.take_damage(d)

        return 'You attacked the ' + dragon.name + ' with your bow for '  + str(d) + ' damage.'
