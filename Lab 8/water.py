import pokemon
import random

class Water(pokemon.Pokemon):
    def __init__(self, name = None):
        self._name = super().__init__(name, 1)

        water_names = ['Staryu', 'Magikarp', 'Horsea']
        if self._name == None:
            n = random.randint(0,2)
            self._name = water_names[n]

    '''Override get_special_menu'''
    # display water attacks
    def special_menu(self):
        print("1. Water Gun\n2. Bubble Beam")

    # water gun special attack
    def _water_gun(self, opponent):
        damage = random.randint(1,7)

        # water vs fire: super effective
        if opponent._type == 0:
            damage *= 2
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with a WATER GUN for {damage} damage. \
                It was SUPER EFFECTIVE!'
        
        # water vs water: not very effective
        elif opponent._type == 1:
            damage *= 0.5
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with a WATER GUN for {damage} damage. \
                It was not very effective.'
    
        # water vs grass: not very effective
        else:
            damage *= 0.5
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with a WATER GUN for {damage} damage. \
                It was not very effective.'

    # water blast special attack
    def _bubble_beam(self, opponent):
        damage = random.randint(3,5)

        # water vs fire: super effective
        if opponent._type == 0:
            damage *= 2
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with a BUBBLE BEAM for {damage} damage. \
                It was SUPER EFFECTIVE!'
        
        # water vs water: not very effective
        elif opponent._type == 1:
            damage *= 0.5
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with a BUBBLE BEAM for {damage} damage. \
                It was not very effective.'
    
        # water vs grass: not very effective
        else:
            damage *= 0.5
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with a BUBBLE BEAM for {damage} damage. \
                It was not very effective.'