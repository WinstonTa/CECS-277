import check_input
import random

def reset_game():
  """Resets the game board and the solution board.  Blanks out both boards, 
  then places a new ship at a random location on the solution board.  
  Returns both boards."""
  
 
    
def display_board(board):
  """Displays the state of the game board as a 5x5 grid where rows are labeled 
  with the letters A-E and columns are labeled with the values 1-5."""
  game_board = [[' ','1','2','3','4','5'],
                ['A','~','~','~','~','~'],
                ['B','~','~','~','~','~'],
                ['C','~','~','~','~','~'],
                ['D','~','~','~','~','~'],
                ['E','~','~','~','~','~']]
  

def get_row():
  """Prompts the user to enter a row letter selection, repeats until user 
  enters a valid selection, returns that value."""

  
def fire_shot(grid, solution, row, col):
  """Places a hit or a miss on the game board.  Passes in both the grid and 
  solution boards and the user's entry for the row and column.  Inspects that 
  location on the solution board to determine whether to place a '*' for a 
  hit, or a 'x' for a miss."""


def main():
  

if __name__ == '__main__':
    main()