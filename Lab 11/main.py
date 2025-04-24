'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/04/24
Description: This project lets users build a character that will fight three different monsters. Choosing between
a bard, warrior, or wizard, they can use 2 items from a shield, ring, or cloak to defeat 2 of 3 minimum trials to win.
'''

# file imports
import random
import check_input
import bard
import character
import cloak
import our_decorator
import ring
import shield
import warrior
import wizard

# main game functionality
def main():
    print("Character Maker!")

    player = None
    character_choice = check_input.get_int_range("Choose a starting character:\n1. Bard\n2. Warrior\n3. Wizard\n", 1, 3)
    enemies = {
        "Spiked Dragon": (0, 6),
        "Orc Warlord": (1, 5),
        "Shadow Knight": (2, 4),
        "Lava Monster": (3, 3),
        "Fiendish Ghoul": (4, 2),
        "Goblin Mage": (5, 1),
        "Dark Magician": (6, 0)
    }
    enemy_selection = list(random.sample(sorted(enemies.items()), 3))
    
    match character_choice:
        case 1:
            player = bard.Bard()
            print(f"\n{player}")
        case 2:
            player = warrior.Warrior()
            print(f"\n{player}")
        case 3:
            player = wizard.Wizard()
            print(f"\n{player}")

    magic_items = ["Sturdy Shield", "Magic Ring", "Protective Cloak"]
    items_left = 2

    while items_left > 0:
        print(f"Choose {items_left} items:")
        for i, magic_item in enumerate(magic_items):
            print(f"{i + 1}. {magic_item}")
        decoration_choices = check_input.get_int_range("", 1, len(magic_items))

        match magic_items[decoration_choices - 1]:
            case "Sturdy Shield":
                player = shield.Shield(player)
            case "Magic Ring":
                player = ring.Ring(player)
            case "Protective Cloak":
                player = cloak.Cloak(player)

        magic_items.remove(magic_items[decoration_choices - 1])
        items_left -= 1
        print(f"\n{player}")
    
    current_enemy = random.choice(enemy_selection)
    print("You must pass two of the following three trials!\nTrial 1 of 3:")
    print(f"You encounter a {current_enemy[0]}\nMR: {current_enemy[1][0]}\nStrength: {current_enemy[1][1]}")

# execute main game
if __name__ == "__main__":
    main()
