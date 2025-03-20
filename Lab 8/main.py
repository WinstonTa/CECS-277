'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/03/20
Description: Create a pokemon trainer game where the user must defeat three pokemon to become a pokemon master.
Uses inheritance to implement different types of pokemon.
'''

import check_input
import fire
import grass
import pokemon
import water
import random

def main():

    # creating list of random pokemon to fight
    pokemon_list = [fire.Fire(), water.Water(), grass.Grass()]

    print(f"PROF OAK: Hello Trainer! Today you're off to fight your first battle of 1 vs. 3 pokemon. \
          \n1. {pokemon_list[0]}\n2. {pokemon_list[1]}\n3. {pokemon_list[2]}")

    # having user select what pokemon they will fight with
    fighter = check_input.get_int_range("Select the pokemon that you will battle with. \
               \n1. I choose you, Charmander\n2. Squirtle! GO!\
               \n3. We can do it together Bulbasaur!\
               \nPlease choose a pokemon: ",1,3)
    
    if fighter == 1:
        mon = fire.Fire('Charmander')
    elif fighter == 2:
        mon = water.Water('Squirtle')
    else:
        mon = grass.Grass('Bulbasaur')

    print("\n  -- TRAINER BATTLE --")

    while len(pokemon_list) > 0 and mon.hp > 0:

        # what pokemon trainer will attack, trainer's pokemon
        print(f"TRAINER: I choose you: \n{pokemon_list[0]}\n\n{mon}\n")

        # choosing normal or special attack
        attack_type = check_input.get_int_range("1. Normal Attack\n2. Special Attack\nEnter attack type: ", 1, 2)

        # normal attack
        if attack_type == 1:
            normal_attack = check_input.get_int_range("Choose a Move:\n1. Slam\n2. Tackle\nEnter move: ", 1, 2)
            print(mon._normal_move(pokemon_list[0], normal_attack))
        
        # special attack
        if attack_type == 2:
            special_attack = check_input.get_int_range(mon.get_special_menu(), 1, 2)
            print(mon._special_move(pokemon_list[0], special_attack))
        
        # opponent pokemon strikes back
        print(pokemon_list[0]._special_move(mon, random.randint(1, 2)))

        # pokemon dies, remove it from list
        if pokemon_list[0].hp == 0:
            pokemon_list.remove(pokemon_list[0])
            print("TRAINER: NOOOO! You defeated my pokemon!")
        if mon.hp == 0:
            print("TRAINER: HA! I defeated you, come back when you get a better pokemon...")

if __name__ == '__main__':
    main()
