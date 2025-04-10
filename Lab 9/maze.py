class Maze:
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

        for i in range(len(maze)):
            row = list(maze[i])
            maze.append(row)
                
        self._m = maze

    def __getitem__(self, row):
        return self._m[row]
    
    def is_wall(self, r, c):
        # check to see if comparison should be "==" or "is" or "contains"
        return self._m[r][c] == "*"
    
    def place_char(self, r, c, char):
        self._m[r][c] = char
    
    def __str__(self):
        maze_grid = list(list())
        for i in range(len(self._m)):
            for j in range(len(self._m.__getitem__(i))):
                maze_grid[i][j] = self._m[i][j]
        return str(maze_grid)
    
    def search_maze(self, char):
        row_coord = -1
        col_coord = -1
        coordinates = [row_coord, col_coord]

        for row in self._m:
            for col in self._m:
                if self._m[row][col] == char:
                    row_coord = row
                    col_coord = col
        
        return coordinates
    
    def count_dots(self) -> int:
        dot_count = 0
        for row in self._m:
            for col in self._m:
                if self._m[row][col] == ".":
                    dot_count += 1
        
        return dot_count
