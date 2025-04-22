import our_decorator

class Cloak(our_decorator.Decorator):
    def description(self):
        return "Cloaked" + super().description()

    def magic_resistance(self):
        return super().magic_resistance() + 1

    def strength(self):
        return super().strength() + 1
