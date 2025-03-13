import dragon

class FlyingDragon(dragon.Dragon()):

    def __init__(self, name, hp):
        super().__init__(name, hp)
        self._swoops = 3

    def special_attack(self, hero):
        pass

    def __str__(self):
        pass