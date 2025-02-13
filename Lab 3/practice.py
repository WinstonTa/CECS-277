import main

game_board = []
game_board.append(['  1 2 3 4 5'])

alpha = ['A','B','C','D','E']
blank_board = '~~~~~'

for i in range(5):
    game_board.append(f"{alpha[i]}{blank_board}")


print(game_board)
main.display_board(game_board)
