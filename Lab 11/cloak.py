import decorator

class Cloak(decorator.Decorator):
    def description(self):
        return "Protective Cloak"

    def magic_resistance(self):
        return super().magic_resistance() + 1

    def strength(self):
        return super().strength() + 1
