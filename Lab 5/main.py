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
    
    rect_width=check_input.get_int_range("Enter rectangle width (1-5): ",1,5)
    rect_height=check_input.get_int_range("Enter rectangle height (1-5): ")

    while True:
        user_choice=check_input.get_int_range("Enter Direction:\n1.Up\n2.Down\n3.Left\n4.Right\n5.Quit",1,5)
        
        if user_choice == 1:
            pass     
        elif user_choice == 2:
            pass
        elif user_choice == 3:
            pass
        elif user_choice == 4:
            pass
        else:
            return False


if __name__ == "__main__":
    main()
