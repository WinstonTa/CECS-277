import random

class Ghost:
    def __init__(self):
        self._previous = '.'
    
    def move(self) -> bool:
        # direction ghost should move next, collision variable
        x_move = 0
        y_move = 0
        collision = False

        # initialize maze, find player and ghost coordinates
        maze = maze()
        player_location = maze.search_maze("P")
        ghost_location = maze.search_maze("G")

        # check player position relative to ghost position: x-coordinate
        if player_location[0] < ghost_location[0]:
            x_move = 1
        elif player_location[0] > ghost_location[0]:
            x_move = -1
        else:
            pass
        
        # check player position relative to ghost position: y-coordinate
        if player_location[1] < ghost_location[1]:
            y_move = 1
        elif player_location[1] > ghost_location[1]:
            y_move = -1
        else:
            pass

        # check if ghost movement will collide with wall, choose new direction if so
        if maze.is_wall(ghost_location[0] + x_move, ghost_location[1] + y_move):
            ghost_location[0] + x_move 

        # update ghost location
        ghost_location[0] += x_move
        ghost_location[1] += y_move

        # test if player location matches ghost location, update collision if so
        if player_location == ghost_location:
            collision = True
        
        return collision
