import pokemon
import random

class Grass(pokemon.Pokemon):
    def __init__(self, name = None):
        self._name = super().__init__(name, 2)

        grass_names = ['Oddish', 'Bellsprout', 'Exeggcute']
        if self._name == None:
            n = random.randint(0,2)
            self._name = grass_names[n]

    '''Override get_special_menu'''
    # display grass attacks
    def special_menu(self):
        print("1. Razor Leaf\n2. Solar Beam")

    # grass special attack
    def _razor_leaf(self, opponent):
        damage = random.randint(3,5)

        # grass vs fire: not very effective
        if opponent._type == 0:
            damage *= 0.5
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with SOLAR BEAM for {damage} damage. \
                It was not very effective'
        
        # grass vs water: super effective
        elif opponent._type == 1:
            damage *= 2
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with SOLAR BEAM for {damage} damage. \
                It was SUPER EFFECTIVE!'
    
        # grass vs grass: not very effective
        else:
            damage *= 0.5
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with SOLAR BEAM for {damage} damage. \
                It was not very effective.'

    # water blast special attack
    def _solar_beam(self, opponent):
        damage = random.randint(2,6)

        # grass vs fire: not very effective
        if opponent._type == 0:
            damage *= 0.5
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with SOLAR BEAM for {damage} damage. \
                It was not very effective'
        
        # grass vs water: super effective
        elif opponent._type == 1:
            damage *= 2
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with SOLAR BEAM for {damage} damage. \
                It was SUPER EFFECTIVE!'
    
        # grass vs grass: not very effective
        else:
            damage *= 0.5
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with SOLAR BEAM for {damage} damage. \
                It was not very effective.'