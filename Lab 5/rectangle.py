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
        self.y -= 1
    
    def move_down(self):
        """moves the rectangle down one row"""
        self.y += 1
    
    def move_left(self):
        """moves the rectangle left one column"""
        self.x -= 1

    def move_right(self):
        """moves the rectangle right one column"""
        self.x += 1
