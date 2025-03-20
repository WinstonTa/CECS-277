import pokemon
import random

class Water(pokemon.Pokemon):
    def __init__(self, name = None):
        if name == None:
            name = random.choice(['Staryu', 'Magikarp', 'Horsea'])
        super().__init__(name, p_type = 1)
    
    '''Override get_special_menu'''
    # display water attacks
    def get_special_menu(self):
        return "1. Water Gun\n2. Bubble Beam\nEnter move: "
    
    def _special_move(self, opponent, move):
        if move == 1:
            return self._water_gun(opponent)
        else:
            return self._bubble_beam(opponent)
    
    # water gun special attack
    def _water_gun(self, opponent):
        damage = random.randint(1,7)

        # water vs fire: super effective
        if opponent._p_type == 0:
            damage *= 2
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with a WATER GUN for {damage} damage. It was SUPER EFFECTIVE!'
        
        # water vs water: not very effective
        elif opponent._p_type == 1:
            damage *= 0.5
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with a WATER GUN for {damage} damage. It was not very effective.'
    
        # water vs grass: not very effective
        else:
            damage *= 0.5
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with a WATER GUN for {damage} damage. It was not very effective.'

    # water blast special attack
    def _bubble_beam(self, opponent):
        damage = random.randint(3,5)

        # water vs fire: super effective
        if opponent._p_type == 0:
            damage *= 2
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with a BUBBLE BEAM for {damage} damage. It was SUPER EFFECTIVE!'
        
        # water vs water: not very effective
        elif opponent._p_type == 1:
            damage *= 0.5
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with a BUBBLE BEAM for {damage} damage. It was not very effective.'
    
        # water vs grass: not very effective
        else:
            damage *= 0.5
            opponent._take_damage(damage)
            return f'{self._name} blasts {opponent._name} with a BUBBLE BEAM for {damage} damage. It was not very effective.'