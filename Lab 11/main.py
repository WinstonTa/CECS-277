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
    
    for i, (enemies[0], (mr, strength)) in enumerate(enemy_selection, 1):
        current_enemy = random.choice(enemy_selection)
        print(f"You must pass two of the following three trials!\nTrial {i} of 3:")
        print(f"You encounter a {current_enemy[0]}\nMR: {current_enemy[1][0]}\nStrength: {current_enemy[1][1]}")
        fight_choice = check_input.get_int_range("Fight\n1. Battle\n2. Dodge\n", 1, 2)
        passed_trial = False
        success_count = 0
        fail_count = 0
        
        if fight_choice == 1:
            if player.magic_resistance() and player.strength() >= (current_enemy[1][0] and current_enemy[1][1]):
                passed_trial = True
            print(f"You battle with the {enemies[0]} and " + ("easily defeat it" if passed_trial else "are easily defeated")\
            + f"\nYou have {'passed' if passed_trial else 'failed'} this trial.")
        else:
            dodge_rate = random.randint(1, 4) == 1
            print(f"You attempt to dodge the {enemies[0]} and " + ("narrowly evade it by the skin of your teeth"\
                if dodge_rate else "it manages to hit you") + f"\nYou have {'passed' if dodge_rate else 'failed'} this trial.")
        
        if passed_trial:
            success_count += 1
        else:
            fail_count += 1
        
        if success_count == 2:
            print("\nWell done, you've successfully passed two of the three trials.")
            break
        if fail_count == 2:
            print("\nYou've failed to complete two out of three tails, return home and come back stronger.")
            break
    
    

# execute main game
if __name__ == "__main__":
    main()
