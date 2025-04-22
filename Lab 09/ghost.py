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
        x_move = 0
        y_move = 0
        collision = False

        m = maze.Maze()
        player_location = m.search_maze("P")
        ghost_location = m.search_maze("G")

        # check row direction (up/down)
        if player_location[0] < ghost_location[0]:
            x_move = -1
        elif player_location[0] > ghost_location[0]:
            x_move = 1

        # check col direction (left/right)
        if player_location[1] < ghost_location[1]:
            y_move = -1
        elif player_location[1] > ghost_location[1]:
            y_move = 1

        # Try to move vertically first
        next_row = ghost_location[0] + x_move
        next_col = ghost_location[1]

        if x_move != 0 and not m.is_wall(next_row, next_col):
            pass  # move is fine
        elif y_move != 0 and not m.is_wall(ghost_location[0], ghost_location[1] + y_move):
            next_row = ghost_location[0]
            next_col = ghost_location[1] + y_move
        else:
            # blocked, try random cardinal directions (no diagonals)
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                if not m.is_wall(ghost_location[0] + dx, ghost_location[1] + dy):
                    next_row = ghost_location[0] + dx
                    next_col = ghost_location[1] + dy
                    break  # take first valid direction

        # restore previous tile
        m.place_char(ghost_location[0], ghost_location[1], self._previous)
        self._previous = m[next_row][next_col]
        m.place_char(next_row, next_col, "G")

        if [next_row, next_col] == player_location:
            collision = True

        return collision
