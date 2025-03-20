import abc
import random

class Pokemon:
    def __init__(self, name, p_type):
        self._name = name
        self._p_type = p_type
        self._hp = 25
        self._battle_table = [[1, .5, 2], [2, 1, .5], [.5, 2, 1]]
    
    @property
    def hp(self):
        """accesses the hp property and returns it (accessor)"""
        return self._hp

    def get_normal_menu(self) -> str:
        """returns a string with the menu options for the normal moves: slam and tackle."""
        return "Choose an Attack Type:\n1. Normal\n2. Special\nEnter attack type: "

    def _normal_move(self, opponent, move) -> str:
        """use the move parameter to choose to call either slam or tackle method,
        returns the string returned from those methods."""
        return "Choose a Move:\n1. Slam\n2. Tackle\nEnter move: "

    def _slam(self, opponent) -> str:
        """randomize some damage (slam 2-6, tackle 3-5),
        call take_damage on the opponent,
        and return a string description of the move using both pokemons’ names,
        the name of the move, and the amount of damage taken."""
        slam_dmg = random.randint(2, 6)
        opponent._take_damage(slam_dmg)
        return f"{self._name} SLAMS {opponent._name} for {slam_dmg} damage."

    def _tackle(self, opponent) -> str:
        """randomize some damage (slam 2-6, tackle 3-5),
        call take_damage on the opponent,
        and return a string description of the move using both pokemons’ names,
        the name of the move, and the amount of damage taken."""
        tackle_dmg = random.randint(3, 5)
        opponent._take_damage(tackle_dmg)
        return f"{self._name} TACKLES {opponent._name} for {tackle_dmg} damage."

    @abc.abstractmethod
    def get_special_menu(self) -> str:
        """uses the move parameter to choose to call either of the special moves for that pokemon type."""
        return "1. special move 1\n2. special move 2\nEnter move: "

    def attack(self, opponent, type, move):
        """use the type parameter to choose to call either _normal_move or _special_move
        and pass it the opponent and move parameters."""
        if type == "normal move":
            self._normal_move()
        elif type == "special move":
            self._special_move()
        else:
            pass

    def __str__(self):
        """display the pokemon’s name and hp in the format “Name: hp/25”."""
        return f"{self._name}: {self.hp}/25"

    def _take_damage(self, dmg):
        """the damage the pokemon takes. Subtract the dmg value from the pokemon’s _hp.
        Check that the _hp doesn’t go past 0 (if it’s negative, reset it to 0)."""

        # subtract damage from pokemon hp
        self._hp -= dmg

        # check hp is 0 or less, in which case it will reset
        if self.hp <= 0:
            self.hp = 0
