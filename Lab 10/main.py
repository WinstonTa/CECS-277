'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/04/17
Description: This project lets users battle three monsters through Monster Trials to test their adventuring and PVP
ingenuity. They must deal with goblins and trolls, and when done horrible goblins and angry trolls!
'''


# file import nightmare
import entity
import hero
import enemy_factory
import beg_factory
import exp_factory
import beg_goblin
import beg_troll
import exp_troll
import exp_goblin
import check_input


# main game functionality
def main():
    print("Monster Trials")

    # creating a hero
    name = input("What is your name? ")
    winston = hero.Hero(name)
    print(f"You will face a series of 3 monsters, {name}.\nDefeat them all to win.\n")

    # creating monster factories and monster objects
    beginner_factory = beg_factory.BeginnerEnemyFactory()
    expert_factory = exp_factory.ExpertEnemyFactory()

    beg_enemy_1 = beginner_factory.create_random_enemy()
    beg_enemy_2 = beginner_factory.create_random_enemy()
    exp_enemy = expert_factory.create_random_enemy()

    enemies = [beg_enemy_1, beg_enemy_2, exp_enemy]

    game = True
    while game == True:
        # choosing an enemy to attack
        print("Choose an enemy to attack:")
        for i, name in enumerate(enemies):
            print(f"{i + 1}. {enemies[i]}")
        enemy_to_attack = check_input.get_int_range("Enter choice: ", 1, len(enemies)) - 1      # -1 to be able to index later

        # hero chooses weapon they want to use
        print(f"\n{winston}")
        chosen_weapon = check_input.get_int_range("1. Sword Attack\n2. Arrow Attack\nEnter choice: ", 1, 2)

        if chosen_weapon == 1:
            print(winston.melee_attack(enemies[enemy_to_attack]))
        else:
            print(winston.ranged_attack(enemies[enemy_to_attack]))

        # if the enemy is alive, it can counterattack
        if enemies[enemy_to_attack]._hp > 0:
            print(enemies[enemy_to_attack].melee_attack(winston))

        # removing monsters from enemy list if defeated
        for i in range(len(enemies)):
            if enemies[i - 1]._hp == 0:
                print(f"You have slain the {enemies[i - 1]._name}")
                enemies.remove(enemies[i - 1])

        # checking if the battle can continue
        if len(enemies) == 0:
            print("Congratulations! You defeated all three monsters!")
            game = False
        elif winston._hp == 0:
            print("Oh no, you died. Better luck in the next life...")
            game = False

    

# execute main game
if __name__ == "__main__":
    main()

