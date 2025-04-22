import character

class Warrior(character.Character):
    def description(self):
        return f"Name: Harcor the Warrior\nMR: 0\nSTR: 4"
    
    def magic_resistance(self) -> int:
        return 0
    
    def strength(self) -> int:
        return 4
