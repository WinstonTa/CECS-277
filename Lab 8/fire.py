import pokemon
import random

class Fire(pokemon.Pokemon):
    def __init__(self, name = None):
        self._name = super().__init__()
        self._type = 0

        fire_names = ['Ponyta', 'Growlithe', 'Vulpix']
        if self._name == None:
            n = random.randint(0,2)
            self._name = fire_names[n]

    def _ember(self, opponent):
        damage = random.randint(2,6)

        # fire vs fire: not very effective
        if opponent._type == 0:
            damage *= 0.5
            opponent._hp -= damage
            return f'{self._name} BURNS {opponent._name} with EMBERS for {damage} damage. \
                It was not very effective.'
        
        # fire vs water: not very effective
        elif opponent._type == 1:
            damage *= 0.5
            opponent._hp -= damage
            return f'{self._name} BURNS {opponent._name} with EMBERS for {damage} damage. \
                It was not very effective.'
    
        # fire vs grass: super effective
        else:
            damage *= 2
            opponent._hp -= damage
            return f'{self._name} BURNS {opponent._name} with EMBERS for {damage} damage. \
                It was SUPER EFFECTIVE!'

    def _fire_blast(self, opponent):
        damage = random.randint(1,7)

        # fire vs fire: not very effective
        if opponent._type == 0:
            damage *= 0.5
            opponent._hp -= damage
            return f'{self._name} uses FIRE BLAST against {opponent._name} for {damage} damage. \
                It was not very effective.'
        
        # fire vs water: not very effective
        elif opponent._type == 1:
            damage *= 0.5
            opponent._hp -= damage
            return f'{self._name} uses FIRE BLAST against {opponent._name} for {damage} damage. \
                It was not very effective.'
    
        # fire vs grass: super effective
        else:
            damage *= 2
            opponent._hp -= damage
            return f'{self._name} uses FIRE BLAST against {opponent._name} for {damage} damage. \
                It was SUPER EFFECTIVE!'