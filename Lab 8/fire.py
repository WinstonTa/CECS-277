import pokemon
import random

class Fire(pokemon.Pokemon):
    def __init__(self, name = None):
        if name == None:
            name = random.choice(['Ponyta', 'Growlithe', 'Vulpix'])
        super().__init__(name, p_type = 0)
        self.type = 0

    '''Override get_special_menu'''
    # display fire attacks
    def get_special_menu(self):
        return "1. Ember\n2. Fire Blast\nEnter move: "
    
    def _special_move(self, opponent, move):
        if move == 1:
            return self._ember(opponent)
        else:
            return self._fire_blast(opponent)
    
    # ember special attack
    def _ember(self, opponent):
        damage = random.randint(2,6)

        # fire vs fire: not very effective
        if opponent._p_type == 0:
            damage //= 2
            opponent._take_damage(damage)
            return f'{self._name} BURNS {opponent._name} with EMBERS for {damage} damage. It was not very effective.'
        
        # fire vs water: not very effective
        elif opponent._p_type == 1:
            damage //= 2
            opponent._take_damage(damage)
            return f'{self._name} BURNS {opponent._name} with EMBERS for {damage} damage. It was not very effective.'
    
        # fire vs grass: super effective
        else:
            damage *= 2
            opponent._take_damage(damage)
            return f'{self._name} BURNS {opponent._name} with EMBERS for {damage} damage. It was SUPER EFFECTIVE!'

    # fire blast special attack
    def _fire_blast(self, opponent):
        damage = random.randint(1,7)

        # fire vs fire: not very effective
        if opponent._p_type == 0:
            damage //= 2
            opponent._take_damage(damage)
            return f'{self._name} uses FIRE BLAST against {opponent._name} for {damage} damage. It was not very effective.'
        
        # fire vs water: not very effective
        elif opponent._p_type == 1:
            damage //= 2
            opponent._take_damage(damage)
            return f'{self._name} uses FIRE BLAST against {opponent._name} for {damage} damage. It was not very effective.'
    
        # fire vs grass: super effective
        else:
            damage *= 2
            opponent._take_damage(damage)
            return f'{self._name} uses FIRE BLAST against {opponent._name} for {damage} damage. It was SUPER EFFECTIVE!'