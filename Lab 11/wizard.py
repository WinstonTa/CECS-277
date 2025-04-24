import character

class Wizard(character.Character):
    '''extends Character by overriding the three abstract methods and return the values'''

    def description(self):
        return f"Altar the Wizzard"
    
    def magic_resistance(self) -> int:
        return 3
    
    def strength(self) -> int:
        return 1
