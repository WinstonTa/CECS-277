import our_decorator

class Shield(our_decorator.Decorator):
    '''extends Decorator, overrides the three abstract methods and calls each
    method with super and adds on the additional value'''
    
    def description(self):
        return "Shielded " + super().description()

    def magic_resistance(self):
        return super().magic_resistance()

    def strength(self):
        return super().strength() + 2
