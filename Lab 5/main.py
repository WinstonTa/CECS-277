'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/02/27
Description: This project allows users to move a rectangle across a 20x20 grid. Using console inputs, the rectangle will
move in the corresponding direction of the user's choice.
'''
import check_input
import rectangle

def display_grid(grid: list[list[str]]):
    """"
    pass in the grid and display the contents of the grid.

    Args:
        grid (List[List[str]]): the 2D grid that the rectangle can be placed in
    """
    for row in grid:
        for item in row:
            print(item, end = " ")
        print()

def reset_grid(grid: list[list[str]]):
    """
    pass in the grid and overwrite the contents with all ‘.’s

    Args:
        grid (List[List[str]]): the 2D grid that will be reset
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = '. '

def place_rect(grid: list[list[str]], rect: rectangle):
    """
    pass in the grid and the rectangle. At the location of
    the rectangle (x, y) on the grid, overwrite the ‘.’ characters with ‘*’s using the width and
    height of the rectangle.

    Args:
        grid (List[List[str]]): the 2D grid that the rectangle will be placed in
        rect (Rectangle): rectangle object that will be inserted into the grid
    """

    # get rectangle info
    x, y = rect.get_coords()
    w, h = rect.get_dimensions()

    # bound check
    if x < 0 or y < 0 or x + w > 20 or y + h > 20:
        print("ERROR: Rectangle does not fit in the grid.")
        return
    
    # place rectangle in grid
    for i in range(h):
        for j in range(w):
            grid[y + i][x + j] = '* '


def main():

    # create blank grid
    gridspace=[]
    for i in range(20):
        lst=[]
        for j in range(20):
            lst.append(". ")
        gridspace.append(lst)
    
    # take input from user for rectangle width and height
    rect_width=check_input.get_int_range("Enter rectangle width (1-5): ",1,5)
    rect_height=check_input.get_int_range("Enter rectangle height (1-5): ",1,5)

    # create rectangle object
    our_rectangle = rectangle.Rectangle(rect_width,rect_height)

    # place rectangle on grid
    place_rect(gridspace, our_rectangle)
    display_grid(gridspace)
    
    while True:
        user_choice=check_input.get_int_range("Enter Direction:\n1.Up\n2.Down\n3.Left\n4.Right\n5.Quit\n",1,5)
        
        # user chooses to move rectangle up
        if user_choice == 1:
            our_rectangle.move_up()
            reset_grid(gridspace)
            place_rect(gridspace, our_rectangle)
            display_grid(gridspace)  

        # user chooses to move rectangle up  
        elif user_choice == 2:
            our_rectangle.move_down()
            reset_grid(gridspace)
            place_rect(gridspace, our_rectangle)
            display_grid(gridspace)

        # user chooses to move rectangle up
        elif user_choice == 3:
            our_rectangle.move_left()
            reset_grid(gridspace)
            place_rect(gridspace, our_rectangle)
            display_grid(gridspace)

        # user chooses to move rectangle up
        elif user_choice == 4:
            our_rectangle.move_right()
            reset_grid(gridspace)
            place_rect(gridspace, our_rectangle)
            display_grid(gridspace)

        # user chooses to move quit program
        else:
            return False


if __name__ == "__main__":
    main()
