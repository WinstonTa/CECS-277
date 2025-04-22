import entity
import random

class Dragon(entity.Entity):
    
    def basic_attack(self, hero: entity) -> str:
        """
        Dragon inflicts basic attack.

        Args:
            hero (entity): the hero (passed in as an entity) that will be hurt through basic attack

        Returns:
            A string describing the basic attack.
        """
        d = random.randint(2, 5)
        hero.take_damage(d)

        return self._name + ' smashes you with their tail for ' + str(d) + ' damage!'

    def special_attack(self, hero: entity) -> str:
        """
        Dragon inflicts special attack.

        Args:
            hero (entity): the hero (passed in as an entity) that will be hurt through special attack

        Returns:
            A string describing the special attack.
        """
        d = random.randint(3, 7)
        hero.take_damage(d)

        return self._name + ' slashes you with their claws for ' + str(d) + ' damage!'
