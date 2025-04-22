import decorator

class Shield(decorator.Decorator):
    def description(self):
        return "Sturdy Shield"

    def magic_resistance(self):
        return super().magic_resistance()

    def strength(self):
        return super().strength() + 2
