'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/05/08
Description: This project creates a puppy simulator program that has two basic functions
to feed or play with the puppy. The puppy will react differently to these functions based on 
which state it is currently in. The puppy has three possible states: asleep, eating, or playing
'''

# file imports
import puppy
import check_input

def main():
    print("Congratulations on your new puppy!")

    # construct puppy object
    pup = puppy.Puppy()

    # while the user does not choose to quit, continue looping the options
    choice = 0
    while choice != 3:

        # display a menu that allows user to feed or play, take user input
        choice = check_input.get_int_range("What would you like to do?\n1. Feed the puppy\n2. Play with the puppy\n3. Quit\nEnter choice: ", 1, 3)

        # if the user chooses 1, feed the puppy
        if choice == 1:
            print(pup.give_food())

        # if the user chooses 2, play with the puppy
        elif choice == 2:
            print(pup.throw_ball())

        # if user chooses 3, quit the program 
        else:
            break

if __name__ == "__main__":
    main()