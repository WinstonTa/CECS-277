import decorator

class Ring(decorator.Decorator):
    def description(self):
        return super().description() + "Magic Ring"

    def magic_resistance(self):
        return super().magic_resistance() + 2

    def strength(self):
        return super().strength()
