'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/04/24
Description: This project lets users build a character that will fight three different monsters. Choosing between
a bard, warrior, or wizard, they can use 2 items from a shield, ring, or cloak to defeat 2 of 3 minimum trials to win.
'''

# file imports
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

    character_choice = check_input.get_int_range("Choose a starting character:\n1. Bard\n2. Warrior\n3. Wizard\n", 1, 3)

    magic_items = ["Sturdy Shield", "Magic Ring", "Protective Cloak"]
    items_left = 2

    while items_left > 0:
        for i, magic_item in enumerate(magic_items):
            print(f"Choose {items_left} items:")
            print(f"{i + 1}. {magic_item}")
        decoration_choices = check_input.get_int_range("", 1, len(magic_items) - 1)
        items_left -= 1
        

# execute main game
if __name__ == "__main__":
    main()
