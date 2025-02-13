import main

game_board = []
solution_board = []

blank_board = ['~','~','~','~','~']

for i in range(5):
    game_board.append(blank_board)
    solution_board.append(blank_board)

# create the battleship
# random.randint(0, 3), random.randint(0, 3)
ship_x, ship_y = 0, 0
solution_board[0][0] = '*'
# solution_board[0][1] = '*'
# solution_board[1][0] = '*'
# solution_board[1][1] = '*'
# solution_board[ship_x][ship_y] = '*'                    # ship top left corner
# solution_board[ship_x][ship_y + 1] = '*'                # ship top right corner
# solution_board[ship_x + 1][ship_y] = '*'                # ship bottom left corner
# solution_board[ship_x +1][ship_y + 1] = '*'             # ship bottom right corner

print(solution_board)
print()
print(game_board)
main.display_board(solution_board)
print()
main.display_board(game_board)
