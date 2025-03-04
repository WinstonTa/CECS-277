'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/03/06
Description: This project allows users to play Yahtzee, by which they can increment their points by getting
a pair, a three-of-a-kind, or a series when rolling 3 dice over consecutive turns.
'''
import check_input
import player
import die

def take_turn(player: Player):
    '''
    roll player dice
    display dice
    check for and display any win types (pair, series, three-of-a-kind)
    display updated score
    '''
    player.roll_dice()
    print(player.__str__())

def main():
    '''
    construct a player object
    repeatedly call take_turn() until user chooses to end game
    display final points at the end of the game
    '''
    pass

if __name__ == '__main__':
    main()
