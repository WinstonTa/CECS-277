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

    x, y = rect.get_coords()
    w, h = rect.get_dimensions()

    if x < 0 or y < 0 or x + w > 20 or y + h > 20:
        print("ERROR: Rectangle does not fit in the grid.")
        return
    
    for i in range(h):
        for j in range(w):
            grid[y + i][x + j] = '*'


def main():
    gridspace=[]
    for i in range(20):
        lst=[]
        for j in range(20):
            lst.append(". ")
        gridspace.append(lst)
    
    rect_width=check_input.get_int_range("Enter rectangle width (1-5): ",1,5)
    rect_height=check_input.get_int_range("Enter rectangle height (1-5): ",1,5)
    our_rectangle = rectangle.Rectangle(rect_width,rect_height)

    display_grid(gridspace)
    
    while True:
        user_choice=check_input.get_int_range("Enter Direction:\n1.Up\n2.Down\n3.Left\n4.Right\n5.Quit\n",1,5)
        
        if user_choice == 1:
            rectangle.move_up()    
        elif user_choice == 2:
            rectangle.move_down()
        elif user_choice == 3:
            rectangle.move_left()
        elif user_choice == 4:
            rectangle.move_right()
        else:
            return False


if __name__ == "__main__":
    main()
