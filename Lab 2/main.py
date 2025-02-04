# main.py
'''
Winston Ta, Mindy Yun
2/4/2025
This project allows the user to play rock paper scissors against a computer. Scores are kept track of 
and the user can choose to keep playing or quit when they want.
'''

import check_input_lab2
import random

def weapon_menu():
        '''Prompts the user to input their choice: (R)ock, (P)aper,
    (S)cissors, or (B)ack. Checks that the user’s input is an R, P, S, or B, displays the
    user’s choice, and then returns the inputted value.'''
        user_choice = input('Choose your weapon: \nR. Rock\nP. Paper\nS. Scissors\nB. Back\n')
        while user_choice!='R' and user_choice!='P' and user_choice!= 'S' and user_choice!='B':
            user_choice = input('Please choose an option R, P, S, or B: ')
        return user_choice

def comp_weapon():
    '''Randomly chooses the computer’s throw, displays the
computer’s choice, and returns an R, P, or S.'''
    comp_randomizer = random.randint(1, 3)
    comp_choice = ""
    if comp_randomizer == 1:
        comp_choice = 'R'
    elif comp_randomizer == 2:
         comp_choice = 'P'
    else:
         comp_choice = 'S'
    return comp_choice

def find_winner(player, comp):
    '''Passes in the player’s and computer’s weapon
choices (R, P, or S), compares the two weapons, displays the result, and then returns
who is the winner of that round (0=Tie, 1=Player, 2=Computer) based on the
following rules.
    a. Rock crushes Scissors
    b. Scissors cuts Paper
    c. Paper covers Rock'''
    results = 0
    if ((player == 'R' and comp == 'S') or (player == 'S' and comp == 'P') or (player == 'P' and comp == 'R')):
        results = 1     # player wins these interactions
    elif ((comp == 'R' and player == 'S') or (comp == 'S' and player == 'P') or (comp == 'P' and player == 'R')):
         results = 2    # computer wins these interactions
    else:
         results = 0   # result is a tie
    return results

def display_scores(p_score, c_score):
    '''Passes in the player and computer
scores and displays them to the console.'''

def main():
    blah=1    



weapon_menu()



