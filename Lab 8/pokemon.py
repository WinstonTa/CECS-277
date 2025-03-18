import abc

class Pokemon:
    def __init__(self, name, p_type):
        self._name = name
        self._p_type = p_type
        _battle_table = [[1, .5, 2], [2, 1, .5], [.5, 2, 1]]
    
    @property
    def hp(self):
        """accesses the hp property and returns it (accessor)"""
        pass

    def get_normal_menu(self):
        """returns a string with the menu options for the normal moves: slam and tackle."""
        pass

    def _normal_move(self, opponent, move):
        """use the move parameter to choose to call either slam or tackle method,
        returns the string returned from those methods."""
        pass

    def _slam(self, opponent):
        """randomize some damage (slam 2-6, tackle 3-5),
        call take_damage on the opponent,
        and return a string description of the move using both pokemons’ names,
        the name of the move, and the amount of damage taken."""
        pass

    def _tackle(self, opponent):
        """randomize some damage (slam 2-6, tackle 3-5),
        call take_damage on the opponent,
        and return a string description of the move using both pokemons’ names,
        the name of the move, and the amount of damage taken."""
        pass

    @abc.abstractmethod
    def get_special_menu(self) -> str:
        """uses the move parameter to choose to call either of the special moves for that pokemon type."""
        pass

    def attack(self, opponent, type, move):
        """use the type parameter to choose to call either _normal_move or _special_move
        and pass it the opponent and move parameters."""
        pass

    def __str__(self):
        """display the pokemon’s name and hp in the format “Name: hp/25”."""
        pass

    def _take_damage(self, dmg):
        """the damage the pokemon takes. Subtract the dmg value from the pokemon’s _hp.
        Check that the _hp doesn’t go past 0 (if it’s negative, reset it to 0)."""
        pass
