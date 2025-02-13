'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/02/13
Description: This project allows the user to play battleship on a 5x5 board with a 2x2 ship. The player can continue to
fire shots until they successfully hit all spots of the ship, or show the solution to quickly find the battleship's spot.
'''

import check_input
import random


def display_board(board):
  """Displays the state of the game board as a 5x5 grid where rows are labeled 
  with the letters A-E and columns are labeled with the values 1-5.

  Args:
    board (List[List[str]]): any 2D list board that the program wishes to display"""
  for row in board:
    for item in row:
      print(item, end = " ")
    print()
    
def reset_game():
  """Resets the game board and the solution board.  Blanks out both boards, 
  then places a new ship at a random location on the solution board.  
  Returns both boards."""
  # blank board, game can be reset to this state
  game_board = []
  game_board.append(['  1 2 3 4 5'])

  alpha = ['A','B','C','D','E']
  blank_board = '~~~~~'

  for i in range(5):
      game_board.append(f"{alpha[i]}{blank_board}")
  
  # create the battleship
  ship_lc = [random.randint(1, 4), random.randint(1, 3)]  # ship top left corner
  ship_rc = [ship_lc[0], ship_lc[1] + 1]                  # ship top right corner
  ship_bl = [ship_lc[0] + 1, ship_lc[1]]                  # ship bottom left corner
  ship_rl = [ship_lc[0] + 1, ship_lc[1] + 1]              # ship bottom right corner

  # initalize game board, initialize it to the blank board
  # game_board = blank_board
  
  # row letters + empty solution grid as a 2D list
  solution_board = [[' ', '1', '2', '3', '4', '5'], [], [], [], [], []]
  columns = [' ', 'A','B','C','D','E']

  # initialize solution grid with battleship placement
  for i in range(1, len(solution_board)):                      # rows
      solution_board[i].append(columns[i])
      for j in range(len(solution_board) - 1):                  # columns
          if [i,j] == ship_lc or [i,j] == ship_rc or \
              [i,j] == ship_bl or [i,j] == ship_rl :
              solution_board[i].append('*')
          else:
              solution_board[i].append('~')


  # return 2 variables: first the game board, second the solution board
  return game_board, solution_board


def get_row():
  """Prompts the user to enter a row letter selection, repeats until user 
  enters a valid selection, returns that value.
  Returns:
    Integer for row number, should be within the integer range from 1-5"""
  
  # user input here, with capitalization for lower case letter inputs
  row_choice = input("Enter a Row Letter (A-E): ").upper()
  row_number = 0

  # while loop handles non-valid user inputs
  while row_choice!='A' and row_choice!='B' and row_choice!= 'C' and \
    row_choice !='D' and row_choice != 'E':
    row_choice = input('Please choose an option A-E: ').upper()

  # row letters are converted to row numbers for final variable return
  if row_choice == 'A':
     row_number = 1
  elif row_choice == 'B':
     row_number = 2
  elif row_choice == 'C':
     row_number = 3
  elif row_choice == 'D':
     row_number = 4
  elif row_choice == 'E':
     row_number = 5
  else:
     row_number = 0
  
  # return row number, previously designated as a letter
  return row_number

  
def fire_shot(grid, solution, row, col):
  """Places a hit or a miss on the game board.  Passes in both the grid and 
  solution boards and the user's entry for the row and column.  Inspects that 
  location on the solution board to determine whether to place a '*' for a 
  hit, or a 'x' for a miss.
  Args:
    grid (List[List[str]]): the grid that the game is in, known as game_board
    solution (List[List[str]]): the solution grid to compare the grid to
    row (int): an integer from 1-5, the row the user fires a shot at
    col (int): an integer from 1-5, the column the user fires a shot at
  Returns:
    True if the user successfully hit a shot on the battleship, False if the user fails at this task"""

  # if user hits same spot twice then console does nothing and notifies user
  if grid[row][col] == '*':
     print("You have already chosen that location.")
     return False

  # adds '*' for successful hits and 'x' for attempted hits
  if solution[row][col] == '*' and grid[row][col] != '*':
    grid[row][col] = '*'
    return True
  else:
    grid[row][col] = 'x'
    return False


def main():
  # display initial board
  game_board, solution_board = reset_game()
  display_board(game_board)
  hit_count = 0
  
  # terminal continues running and on standby for user input
  while True:
    # options menu
    user_choice = check_input.get_int_range("Menu:\n1. Fire Shot\n2. Show Solution\n3. Quit\n", 1, 3)

    if user_choice == 1:
      # user fires shot
      user_row = get_row()
      user_col = check_input.get_int_range("Enter a Column Number (1-5): ", 1, 5)
      if fire_shot(game_board, solution_board, user_row, user_col):
        hit_count += 1
      
      display_board(game_board)

      # victorious user displays winning text and resets game
      if hit_count == 4:
         print("\nYou won!\n")
         game_board, solution_board = reset_game()
         display_board(game_board)
    
    elif user_choice == 2:
      # shows solution and resets game
      display_board(solution_board)
      game_board, solution_board = reset_game()
      display_board(game_board)

    elif user_choice == 3:
      # quits game
      break

if __name__ == '__main__':
    main()
  
