import our_decorator

class Ring(our_decorator.Decorator):
    '''extends Decorator, overrides the three abstract methods and calls each
    method with super and adds on the additional value'''
    
    def description(self):
        return super().description() + " with a magic ring"

    def magic_resistance(self):
        return super().magic_resistance() + 2

    def strength(self):
        return super().strength()
