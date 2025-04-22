import our_decorator

class Shield(our_decorator.Decorator):
    def description(self):
        return "Shielded" + super().description()

    def magic_resistance(self):
        return super().magic_resistance()

    def strength(self):
        return super().strength() + 2
