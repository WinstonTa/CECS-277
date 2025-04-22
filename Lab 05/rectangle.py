class Rectangle:
    # initialize rectangle objects
    def __init__(self, w, h):
        """pass in w and h (not x and y), assign them to width and height, set the x and y attributes to 0"""
        self.x = 0
        self.y = 0
        self.w = w
        self.h = h

    def get_coords(self) -> list:
        """returns the x and y values as a pair (either a tuple or a list)"""
        return [self.x, self.y]
    
    def get_dimensions(self) -> list:
        """returns the rectangle’s width and height as a pair."""
        return [self.w, self.h]
    
    def move_up(self):
        """moves the rectangle up one row"""
        if self.y == 0:
            print("The rectangle is already at the top corner -- it can't be moved up")
        else:
            self.y -= 1
    
    def move_down(self):
        """moves the rectangle down one row"""
        if self.y + self.h >= 20:
            print("The rectangle is already at the bottom corner -- it can't be moved down")
        else:
            self.y += 1
    
    def move_left(self):
        """moves the rectangle left one column"""
        if self.x == 0:
            print("The rectangle is already at the left corner -- it can't be moved left")
        else:
            self.x -= 1

    def move_right(self):
        """moves the rectangle right one column"""
        if self.x + self.w >= 20:
            print("The rectangle is already at the right corner -- it can't be moved right")
        else:
            self.x += 1
