import random
import maze

class Ghost:
    def __init__(self):
        # previous tile will be replaced with '.'
        self._previous = '.'
    
    def move(self) -> bool:
        """
        Ghost moves in directions that gradually pursue the player. If the ghost hits a wall then they will
        move in a random direction to continue pursuing the player.

        Returns:
            A boolean that returns True if the ghost collided into the player, False if the player is safe.
        """
        # direction ghost should move next, collision variable
        x_move = 0
        y_move = 0
        collision = False

        # initialize maze, find player and ghost coordinates
        m = maze()
        player_location = m.search_maze("P")
        ghost_location = m.search_maze("G")

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
        if m.is_wall(ghost_location[0] + x_move, ghost_location[1] + y_move):
            # if in corner
            x_move = random.randint(-1, 1)
            y_move = random.randint(-1, 1)
        elif m.is_wall(ghost_location[0] + x_move, ghost_location[1]):
            # if hit wall on x coordinate
            y_move = random.choice([-1, 1])
        elif m.is_wall(ghost_location[0], ghost_location[1] + y_move):
            # if hit wall on y coordinate
            x_move = random.choice([-1, 1])

        # update ghost location
        ghost_location[0] += x_move
        ghost_location[1] += y_move

        m.place_char(ghost_location[0], ghost_location[1], "G")

        # test if player location matches ghost location, update collision if so
        if player_location == ghost_location:
            collision = True
        
        return collision
