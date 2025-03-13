class Entity():
    def __init__(self, name, max_hp):
        self._max_hp = max_hp
        self._hp = max_hp
    
    def take_damage(self, dmg):
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0

