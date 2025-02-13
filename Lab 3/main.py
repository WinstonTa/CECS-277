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
  
  ship_lc = [random.randint(0,3), random.randint(0,3)]    # ship top left corner
  ship_rc = [ship_lc[0], ship_lc[1] + 1]                  # ship top right corner
  ship_bl = [ship_lc[0] + 1, ship_lc[1]]                  # ship bottom left corner
  ship_rl = [ship_lc[0] + 1, ship_lc[1] + 1]              # ship bottom right corner

  alpha = ['A','B','C','D','E']

  # print solution board
  print('  1 2 3 4 5')
  alpha = ['A','B','C','D','E']
  solution_grid = [[],[],[],[],[],[]]
  for i in range(5):                      # rows
      solution_grid[i].append(alpha[i])
      for j in range(5):                  # columns
          if [i,j] == ship_lc or [i,j] == ship_rc or \
              [i,j] == ship_bl or [i,j] == ship_rl :
              solution_grid[i].append('*')
          else:
              solution_grid[i].append('~')

  '''# this is if we want to print the solution board
  for i in range(5):
      for j in range(6):
          print(solution_grid[i][j], end = ' ')
      print()'''
  
  # print blank game board
  print('  1 2 3 4 5')
  for i in range(5):
    print(alpha[i], end=' ')
    for j in range(5):
      print('~', end = ' ')
    print()


def get_row():
  """Prompts the user to enter a row letter selection, repeats until user 
  enters a valid selection, returns that value."""
  row_choice = input("Enter a Row Letter (A-E): ").upper()
  while row_choice!='A' and row_choice!='B' and row_choice!= 'C' and \
    row_choice !='D' and row_choice != 'E':
    row_choice = input('Please choose an option A-E: ').upper()
  return row_choice

  
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

  solution_board = [[' ','1','2','3','4','5'],
                    ['A','~','~','~','~','~'],
                    ['B','~','~','~','~','~'],
                    ['C','~','~','~','~','~'],
                    ['D','~','~','~','~','~'],
                    ['E','~','~','~','~','~']]

  # terminal continues running and on standby for user input
  while True:
    # options menu
    user_choice = check_input.get_int_range("Menu:\n1. Fire Shot\n2. Show Solution\n3. Quit\n", 1, 3)

    if user_choice == 1:
      # user fires shot
      user_row = get_row()
      user_col = check_input.get_int_range("Enter a Column Number (1-5): ", 1, 5)
      # fire_shot(game_board, solution, user_row, user_col)

    elif user_choice == 2:
      # shows solution and resets game
      reset_game()

    elif user_choice == 3:
      # quits game
      break

    else:
      # handle invalid input
      print('Invalid choice. Please try again')



if __name__ == '__main__':
    main()
  
