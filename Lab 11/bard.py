import character

class Bard(character.Character):
    def description(self) -> str:
        return f"Name: Barth the Bard\nMR: 2\nSTR: 2"
    
    def magic_resistance(self) -> int:
        return 2
    
    def strength(self) -> int:
        return 2
