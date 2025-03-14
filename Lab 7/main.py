'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/03/13
Description: Create a game where the user must defeat three dragons to pass the trails. Use inheritance to
implement the following class diagram in your program.
'''

import entity
import dragon
import fire
import flying
import hero
import check_input
import random

# introduction, create hero
name = input('What is your name, challenger?\n')
winston = hero.Hero(name, 50)
print(f'\nWelcome to dragon training, \n{winston}\nYou must defeat 3 dragons.')

dragons_list = [dragon.Dragon('Deadly Lizzettey', 10), fire.FireDragon('Acefury', 15), flying.FlyingDragon('Windy Mindy', 20)]

# game runs until dragons are dead or hero is dead
while winston.hp > 0 and len(dragons_list) > 0:

    # menu of hero and dragons hp
    for i, d in enumerate(dragons_list):
        print(winston)
        print(f"{i + 1}. {d}") 

    # choosing which dragon to attack with which weapon
    attack_dragon = check_input.get_int_range('Choose a dragon to attack: ', 1, len(dragons_list))
    print('Attack with:\n1. Arrow (1 D12)\n2. Sword (2 D6)')
    weapon = check_input.get_int_range('Enter weapon: ', 1, 2)

    # hero attacks
    if weapon == 1:
        print(winston.arrow_attack(dragons_list[attack_dragon - 1]))
    else:
        print(winston.sword_attack(dragons_list[attack_dragon - 1]))

    # dragon attacks
    random_attack = random.randint(1, len(dragons_list))
    print(dragons_list[random_attack - 1].special_attack(winston))

    # checking if dragon is alive
    for i in range(len(dragons_list)):
        if dragons_list[i].hp <= 0:
            print(f'You defeated the {dragons_list[i]}!')
            dragons_list.remove(dragons_list[i])
            break

    # game ends if all dragons die
    if len(dragons_list) == 0:
        print('Congratulations! You have defeated all 3 dragons, you have passed the trials')

    # game ends if winston dies
    if winston.hp <= 0:
        print(f'It seems the dragons have gotten the best of you. Better luck in the next life {name}')

    


