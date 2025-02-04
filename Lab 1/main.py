import check_input
import random
def main():
    lets_play = True
    user_cash = 100
    print("-Three Card Monte-\nFind the queen to double your bet!")

    while user_cash > 0 and lets_play == True:
        print(f"\n\nYou have ${user_cash}.")
        queen_location = random.randint(1, 3)
        bet_amount = check_input.get_positive_int("Enter desired money amount (integer) to bet: ")

        if bet_amount > user_cash:
            bet_amount = check_input.get_int_range("You actually don't have that much money, bet again: ", 1, user_cash)
        
        print('+-----+ +-----+ +-----+')
        print('| | | | | |')
        print('| 1 | | 2 | | 3 |')
        print('| | | | | |')
        print('+-----+ +-----+ +-----+')

        user_guess = check_input.get_int_range("Guess where the queen is hidden among the 3 cards (enter a value of 1, 2, or 3): ", 1, 3)
        card1, card2, card3 = 'K', 'K','K'
        
        if queen_location == 1:
            card1 = 'Q'
        elif queen_location == 2:
            card2 = 'Q'
        elif queen_location == 3:
            card3 = 'Q'
        
        print('+-----+ +-----+ +-----+')
        print('| | | | | |')
        print(f'| {card1} | | {card2} | | {card3} |')
        print('| | | | | |')
        print('+-----+ +-----+ +-----+')

        if user_guess == queen_location:
            user_cash += bet_amount
            print(f"Congratulations! You got the bet right. The queen's location was {queen_location}, and you guessed {user_guess}!")
            lets_play = check_input.get_yes_no("You're not broke yet so... wanna play again? (y/n): ")
        else:
            user_cash -= bet_amount
            print(f"You lose!! You got the bet WRONG. The queen's location was {queen_location}, and you guessed {user_guess}!")
            if user_cash > 0:
                lets_play = check_input.get_yes_no("You're not broke yet so... wanna play again? (y/n): ")
            else:
                print("You're BROKE. Sorry, game over.")
                lets_play = False
main()
