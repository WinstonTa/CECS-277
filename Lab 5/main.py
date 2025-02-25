'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/02/27
Description: This project allows users to move a rectangle across a 20x20 grid. Using console inputs, the rectangle will
move in the corresponding direction of the user's choice.
'''
import check_input
import rectangle

def display_grid(grid):
    """"pass in the grid and display the contents of the grid."""
    for row in grid:
        for item in row:
            print(item, end = " ")
        print()

def reset_grid(grid):
    """pass in the grid and overwrite the contents with all ‘.’s"""
    for row in grid:
        for item in row:
            print(".", end = " ")
        print()

def place_rect(grid, rect):
    """pass in the grid and the rectangle. At the location of
    the rectangle (x, y) on the grid, overwrite the ‘.’ characters with ‘*’s using the width and
    height of the rectangle."""

def main():
    gridspace=[]
    for i in range(20):
        lst=[]
        for j in range(20):
            lst.append(". ")
        gridspace.append(lst)
    
    display_grid(gridspace)



if __name__ == "__main__":
    main()
