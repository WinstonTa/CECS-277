'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/03/06
Description: This project allows users to play Yahtzee, by which they can increment their points by getting
a pair, a three-of-a-kind, or a series when rolling 3 dice over consecutive turns.
'''
import check_input
import player
import die

def take_turn(player: player):
    '''
    roll player dice
    display dice
    check for and display any win types (pair, series, three-of-a-kind)
    display updated score
    '''
    player.roll_dice()
    print(player.__str__())

    # checks for any win types and prints congratulatory message
    if player.has_pair():
        print("You got a pair!")
    elif player.has_three_of_a_kind():
        print("You got 3 of a kind!")
    elif player.has_series():
        print("You got a series of 3!")
    else:
        print("Aww. Too Bad.")
    
    print(f"Score = {player.points()}")


def main():
    '''
    construct a player object
    repeatedly call take_turn() until user chooses to end game
    display final points at the end of the game
    '''
    # initialize player and play again status
    player = player()
    play_again = True

    print("-Yahtzee-\n")
    while True:
        take_turn(player)
        play_again = check_input.get_yes_no()

        # end the game if the user decides to stop playing
        if not play_again:
            break


if __name__ == '__main__':
    main()
