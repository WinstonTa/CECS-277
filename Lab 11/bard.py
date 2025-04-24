import character

class Bard(character.Character):
    '''extends Character by overriding the three abstract methods and return the values'''
    
    def description(self) -> str:
        return f"Barth the Bard"
    
    def magic_resistance(self) -> int:
        return 2
    
    def strength(self) -> int:
        return 2
