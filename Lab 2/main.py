'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/02/06
Description: This project allows the user to play rock paper scissors against a computer. Scores are kept track of 
and the user can choose to keep playing or quit when they want.
'''

import check_input_lab2
import random

def weapon_menu():
    '''
    Prompts the user to input their choice: (R)ock, (P)aper,
    (S)cissors, or (B)ack. Checks that the user’s input is an R, P, S, or B, displays the
    user’s choice, and then returns the inputted value.
    '''

    user_choice = input('Choose your weapon: \nR. Rock\nP. Paper\nS. Scissors\nB. Back\n')
    while user_choice!='R' and user_choice!='P' and user_choice!= 'S' and user_choice!='B':
        user_choice = input('Please choose an option R, P, S, or B: ')
    if user_choice == 'R':
        return 'Rock'
    elif user_choice == 'P':
        return 'Paper'
    elif user_choice == 'S':
        return 'Scissors'
    else:
        return 'B'

def comp_weapon():
    '''
    Randomly chooses the computer’s throw, displays the
    computer’s choice, and returns an R, P, or S.
    '''

    comp_randomizer = random.randint(1, 3)
    comp_choice = ""
    if comp_randomizer == 1:
        comp_choice = 'Rock'
    elif comp_randomizer == 2:
        comp_choice = 'Paper'
    else:
        comp_choice = 'Scissors'
    return comp_choice

def find_winner(player, comp):
    '''
    Passes in the player’s and computer’s weapon
    choices (R, P, or S), compares the two weapons, displays the result, and then returns
    who is the winner of that round (0=Tie, 1=Player, 2=Computer) based on the
    following rules.

    a. Rock crushes Scissors
    b. Scissors cuts Paper
    c. Paper covers Rock

    Args:
        player (str): player input (should be Rock, Paper, or Scissors)
        comp (str): computer input (should be Rock, Paper, or Scissors)
    
    Returns:
        Integer of 0, 1, or 2 denoting the game's outcome.
    '''

    if ((player == 'Rock' and comp == 'Scissors') or (player == 'Scissors' and comp == 'Paper') or (player == 'Paper' and comp == 'Rock')):
        return 1     # player wins these interactions
    elif ((comp == 'Rock' and player == 'Scissors') or (comp == 'Scissors' and player == 'Paper') or (comp == 'Paper' and player == 'Rock')):
        return 2    # computer wins these interactions
    else:
        return 0   # result is a tie

def display_scores(p_score, c_score):
    '''
    Passes in the player and computer scores and displays them to the console.

    Args:
        p_score (int): player's current score
        c_score (int): computer's current score
    '''

    print(f'Player = {p_score}')
    print(f'Computer = {c_score}')

def main():
    # initialize user and computer scores
    user_score = 0
    comp_score = 0

    while True:
        # Display the main menu and get the user's choice
        print("RPS Menu:")
        print("1. Play Game")
        print("2. Show Score")
        print("3. Quit")
        choice = check_input_lab2.get_int_range("Enter your choice: ", 1, 3)
        
        if choice == 1:
            # play the game
            user_selection = None
            while user_selection != 'B':
                # game logic
                user_selection = weapon_menu()
                computer_selection = comp_weapon()
                winner = find_winner(user_selection, computer_selection)

                if winner == 0:
                    print(f'You chose {user_selection}\nComputer chose {computer_selection}\nTie')
                elif winner == 1:
                    print(f'You chose {user_selection}\nComputer Chose {computer_selection}\nYou win!')
                    user_score += 1
                elif winner == 2:
                    print(f'You chose {user_selection}\nComputer Chose {computer_selection}\nComputer wins')
                    comp_score += 1
        elif choice == 2:
            # display the scores
            display_scores(user_score, comp_score)
        elif choice == 3:
            # quit game and display final scores
            print('Final Score:')
            display_scores(user_score, comp_score)
            break
        else:
            # handle invalid input
            print('Invalid choice. Please try again')


if __name__ == '__main__':
    main()
