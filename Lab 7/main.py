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
winston = input('What is your name, challenger?\n')
winston = hero.Hero(winston, 50)
print(f'\nWelcome to dragon training, \n{winston}\nYou must defeat 3 dragons.')

# create and name dragons
# reg_dragon = dragon.Dragon('Deadly Lizzettey', 10)
# fire_dragon = fire.FireDragon('Acefury', 15)
# wind_dragon = flying.FlyingDragon('Windy Mindy', 20)

# dragons_list = [reg_dragon, fire_dragon, wind_dragon]

dragons_list = [dragon.Dragon('Deadly Lizzettey', 10), fire.FireDragon('Acefury', 15), flying.FlyingDragon('Windy Mindy', 20)]

# while dragons are alive
keep_playing = True

while keep_playing == True:

    # menu of hero and dragons hp

    while winston.hp > 0 and len(dragons_list) > 0:
        print(winston)
        for i, d in enumerate(dragons_list):
            print(str(i + 1) + '. ' + str(d)) 

    # chhoosing which dragon to attack with which wepon
    attack_dragon = check_input.get_int_range('Choose a dragon to attack: ', 1, 3)
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

    # seeing if dragon died
    if dragons_list[0].hp <= 0:
        print(f'You defeated the {dragons_list[0]}!')
        dragons_list.remove(dragons_list[0])
    if dragons_list[1].hp <= 0:
        print(f'You defeated the {dragons_list[1]}!')
        dragons_list.remove(dragons_list[1])
    if dragons_list[2].hp <= 0:
        print(f'You defeated the {dragons_list[2]}!')
        dragons_list.remove(dragons_list[2])

    # game ends if all dragons die
    if len(dragons_list) == 0:
        print('Congratulations! You have defeated all 3 dragons, you have passed the trials')
        keep_playing = False

    # game ends if winston dies
    if winston.hp <= 0:
        print(f'It seems the dragons have gotten the best of you. Better luck in the next life {winston}')
        keep_playing = False

    


