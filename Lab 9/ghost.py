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
        m = maze.Maze()
        player_location = m.search_maze("P")
        ghost_location = m.search_maze("G")

        # check player position relative to ghost position: x-coordinate
        if player_location[0] < ghost_location[0]:
            x_move = -1
        elif player_location[0] > ghost_location[0]:
            x_move = 1
        
        # check player position relative to ghost position: y-coordinate
        if player_location[1] < ghost_location[1]:
            y_move = -1
        elif player_location[1] > ghost_location[1]:
            y_move = 1
        
        # next row and column
        next_row = ghost_location[0] + x_move
        next_col = ghost_location[1] + y_move

        # check if ghost movement will collide with wall, choose new direction if so
        if m.is_wall(next_row, next_col):
            # if in corner
            x_move = random.choice([-1, 0, 1])
            y_move = random.choice([-1, 0, 1])
            next_row = ghost_location[0] + x_move
            next_col = ghost_location[1] + y_move

        # restore previous tile of former ghost location
        m.place_char(ghost_location[0], ghost_location[1], self._previous)

        # save tile that ghost will move to
        self._previous = m[next_row][next_col]

        # move the ghost
        m.place_char(next_row, next_col, "G")

        # test for ghost-player collision
        if [next_row, next_col] == player_location:
            collision = True
        
        return collision
