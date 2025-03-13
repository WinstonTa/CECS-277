class Entity():
    def __init__(self, name, max_hp):
        """Initializes Entity"""
        self._max_hp = max_hp
        self._name = name
        self._hp = max_hp
    
    @property
    def name(self):
        """Accesses the name property."""
        return self._name
    
    @property
    def hp(self):
        """Accesses the hp property."""
        return self._hp

    def take_damage(self, dmg: int):
        """
        Entity takes damage from foreign source.

        Args:
            dmg (int): the amount of damage for the poor victim to take
        """
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0

    def __str__(self):
        """returns information on the entity's name, current hp, and maximum hp"""
        return self._name + ': ' + str(self._hp) + '/' + str(self._max_hp)
