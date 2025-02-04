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
        while user_choice!='R','P','S','B':
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

def display_scores(p_score, c_score):
    '''Passes in the player and computer
scores and displays them to the console.'''

def main():
    blah=1    



weapon_menu()



