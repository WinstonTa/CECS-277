class Maze:
    # singleton implementation
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        # open the file and create the 2D grid
        file = open('Lab 9\\pacman.txt')
        maze = file.readlines()
        maze_grid = []

        # append each string to the maze grid as a list of characters
        for i in range(len(maze)):
            maze_grid.append(list(maze[i]))
                
        self._m = maze_grid

    def __getitem__(self, row: int) -> list:
        """
        Gets the desired row of the grid.

        Args:
            row (int): An integer corresponding to the desired row of the Pacman grid.

        Returns:
            A list corresponding to the desired row of the Pacman grid.
        """

        return self._m[row]
    
    def is_wall(self, r: int, c: int) -> bool:
        """
        Checks for wall collisions.

        Args:
            r (int): An integer corresponding to the desired row of the Pacman grid.
            c (int): An integer corresponding to the desired column of the Pacman grid.

        Returns:
            A boolean that confirms if the player or ghost hit the wall.
        """

        return self._m[r][c] == "*"
    
    def place_char(self, r: int, c: int, char: str):
        """
        Gets the desired row of the grid.

        Args:
            r (int): An integer corresponding to the desired row of the Pacman grid.
            c (int): An integer corresponding to the desired column of the Pacman grid.
        """

        self._m[r][c] = char
    
    def __str__(self):
        # prints maze in grid format
        # for i in range(len(self._m)):
        #     for j in range(len(self._m[i])):
        #         print(self._m[i][j], end='')
        return ''.join(''.join(row) for row in self._m)
    
    def search_maze(self, char: str) -> list:
        """
        Returns the location of the first occurrence of the character in the maze as a two-item 1D list
        (ex. [row, col], or [-1,-1] if not found).

        Args:
            char (str): A character the method will search for.

        Returns:
            A list of the coordinates of the first occurrence of the searched character.
            Will result in [-1, -1] if the character can not be found.
        """
        
        # search for correct character
        for i in range(len(self._m)):
            for j in range(len(self._m[i])):
                if self._m[i][j] == char:
                    return [i, j]
        
        return [-1, -1]
    
    def count_dots(self) -> int:
        # search and count for dots
        dot_count = 0
        for i in range(len(self._m)):
            for j in range(len(self._m[i])):
                if self._m[i][j] == '.':
                    dot_count += 1
        
        return dot_count
