import check_input
import random


def display_board(board):
  """Displays the state of the game board as a 5x5 grid where rows are labeled 
  with the letters A-E and columns are labeled with the values 1-5."""
  for row in board:
    for item in row:
      print(item, end = " ")
    print()
    
def reset_game():
  """Resets the game board and the solution board.  Blanks out both boards, 
  then places a new ship at a random location on the solution board.  
  Returns both boards."""
  game_board = [[' ','1','2','3','4','5'],
                ['A','~','~','~','~','~'],
                ['B','~','~','~','~','~'],
                ['C','~','~','~','~','~'],
                ['D','~','~','~','~','~'],
                ['E','~','~','~','~','~']]
  
  solution_board = [[' ','1','2','3','4','5'],
                ['A','~','~','~','~','~'],
                ['B','~','~','~','~','~'],
                ['C','~','~','~','~','~'],
                ['D','~','~','~','~','~'],
                ['E','~','~','~','~','~']]
  
  return display_board(game_board)
 


def get_row():
  """Prompts the user to enter a row letter selection, repeats until user 
  enters a valid selection, returns that value."""

  
def fire_shot(grid, solution, row, col):
  """Places a hit or a miss on the game board.  Passes in both the grid and 
  solution boards and the user's entry for the row and column.  Inspects that 
  location on the solution board to determine whether to place a '*' for a 
  hit, or a 'x' for a miss."""
  if solution[row][col] == '*' and grid[row][col] != '*':
    grid[row][col] = '*'
    return True
  else:
    grid[row][col] = 'x'
    return False


def main():
  # display initial board
  game_board = [[' ','1','2','3','4','5'],
                ['A','~','~','~','~','~'],
                ['B','~','~','~','~','~'],
                ['C','~','~','~','~','~'],
                ['D','~','~','~','~','~'],
                ['E','~','~','~','~','~']]
  display_board(game_board)

  # terminal continues running and on standby for user input
  while True:
    # options menu
    user_choice = check_input.get_int_range("Menu:\n1. Fire Shot\n2. Show Solution\n3. Quit", 1, 3)

    if user_choice == 1:
      pass
    elif user_choice == 2:
      pass
    elif user_choice == 3:
      pass
    else:
      pass



if __name__ == '__main__':
    main()
