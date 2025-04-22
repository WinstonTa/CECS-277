import pokemon
import random

class Grass(pokemon.Pokemon):
    
    def __init__(self, name = None):
        if name == None:
            name = random.choice(['Oddish', 'Bellsprout', 'Exeggcute'])
        super().__init__(name, p_type = 2)
        self.type = 2
    
    '''Override get_special_menu'''
    # display grass attacks
    def get_special_menu(self):
        return "1. Razor Leaf\n2. Solar Beam\nEnter move: "
    
    def _special_move(self, opponent, move):
        if move == 1:
            return self._razor_leaf(opponent)
        else:
            return self._solar_beam(opponent)
    
    # grass special attack
    def _razor_leaf(self, opponent):
        damage = random.randint(3,5)

        # grass vs fire: not very effective
        if opponent._p_type == 0:
            damage *= 0.5
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with SOLAR BEAM for {damage} damage. It was not very effective'
        
        # grass vs water: super effective
        elif opponent._p_type == 1:
            damage *= 2
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with SOLAR BEAM for {damage} damage. It was SUPER EFFECTIVE!'
    
        # grass vs grass: not very effective
        else:
            damage *= 0.5
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with SOLAR BEAM for {damage} damage. It was not very effective.'

    # water blast special attack
    def _solar_beam(self, opponent):
        damage = random.randint(2,6)

        # grass vs fire: not very effective
        if opponent._p_type == 0:
            damage *= 0.5
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with SOLAR BEAM for {damage} damage. It was not very effective'
        
        # grass vs water: super effective
        elif opponent._p_type == 1:
            damage *= 2
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with SOLAR BEAM for {damage} damage. It was SUPER EFFECTIVE!'
    
        # grass vs grass: not very effective
        else:
            damage *= 0.5
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with SOLAR BEAM for {damage} damage. It was not very effective.'