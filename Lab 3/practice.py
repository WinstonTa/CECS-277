import main

nums = [' ','1','2','3','4','5']
def display_board(board):
  for i in range(4):
    print(nums[i])
    for j in range(4):
      print(j, end = " ")
    print()

game_board = []
solution_board = []

blank_board = ['~','~','~','~','~']
alpha = ['A','B','C','D','E']


for i in range(5):
    game_board.append(blank_board)
    solution_board.append(blank_board)


display_board(game_board)