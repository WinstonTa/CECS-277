import random

class Ghost:
    def __init__(self):
        self._previous = '.'
    
    def move(self) -> bool:
        # direction ghost should move next, collision variable
        x_move = 0
        y_move = 0

        # initialize maze, find player and ghost coordinates
        maze = maze()
        player_location = maze.search_maze("P")
        ghost_location = maze.search_maze("G")

        if player_location[0] < ghost_location[0]:
            x_move = 1
        elif player_location[0] > ghost_location[0]:
            x_move = -1
        else:
            pass
