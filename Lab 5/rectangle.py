class Rectangle:
    # initialize rectangle objects
    def __init__(self, w, h):
        """pass in w and h (not x and y), assign them to width and height, set the x and y attributes to 0"""
        self.x = 0
        self.y = 0
        self.w = w
        self.h = h

    def get_coords(self):
        """returns the x and y values as a pair (either a tuple or a list)"""
    
    def get_dimensions(self):
        """returns the rectangle’s width and height as a pair."""
    
    def move_up(self):
        """moves the rectangle up one row"""
    
    def move_down(self):
        """moves the rectangle down one row"""
    
    def move_left(self):
        """moves the rectangle left one column"""

    def move_right(self):
        """moves the rectangle right one column"""
