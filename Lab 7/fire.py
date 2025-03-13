import dragon

class FireDragon(dragon.Dragon()):

    def __init__(self, name, hp):
        super().__init__(name, hp)
        self._fire_shots = 3

    def special_attack(self, hero):
        if self._fire_shots > 0:
            pass

    def __str__(self):
        pass # super().__str__()