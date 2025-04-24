import character

class Warrior(character.Character):
    '''extends Character by overriding the three abstract methods and return the values'''
   
    def description(self):
        return f"Harcor the Warrior"
    
    def magic_resistance(self) -> int:
        return 0
    
    def strength(self) -> int:
        return 4
