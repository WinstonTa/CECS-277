'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/05/08
Description: This project creates a puppy simulator program that has two basic functions
to feed or play with the puppy. The puppy will react differently to these functions based on 
which state it is currently in. The puppy has three possible states: asleep, eating, or playing
'''

import puppy
import check_input

def main():
    print("Congratulations on your new puppy!")

    pup = puppy.Puppy()

    choice = 0
    while choice != 3:
        # reset how many times puppy has eaten/played in a row
        pup = pup.reset()

        choice = check_input.get_int_range("What would you like to do?\n1. Feed the puppy\n2. Play with the puppy\n3. Quit\nEnter choice: ", 1, 3)

        if choice == 1:
            print(pup.give_food())
            pup = pup.inc_feeds()

        elif choice == 2:
            print(pup.throw_ball())
            pup = pup.inc_plays()

        else:
            break

if __name__ == "__main__":
    main()