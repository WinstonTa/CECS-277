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

        m = maze.Maze()
        # direction ghost should move next, collision variable
        ghost_location = m.search_maze("G")
        x = ghost_location[0]
        y = ghost_location[1]
        collision = False

        # initialize maze, find player and ghost coordinates
        player_location = m.search_maze("P")

        # check player position relative to ghost position: x-coordinate
        if player_location[0] < ghost_location[0]:
            y += -1
        elif player_location[0] > ghost_location[0]:
            y += 1
        
        # check player position relative to ghost position: y-coordinate
        if player_location[1] < ghost_location[1]:
            x += -1
        elif player_location[1] > ghost_location[1]:
            x += 1

        # check if ghost movement will collide with wall, choose new direction if so
        while m.is_wall(x, y):
            x = ghost_location[0]
            y = ghost_location[1]

            random_direction = random.randint(0,1)
            if random_direction == 0:
                x -= random.choice([-1, 1])
            else:
                y -= random.choice([-1, 1])

        # restore previous tile of former ghost location
        m.place_char(ghost_location[0], ghost_location[1], self._previous)

        # save tile that ghost will move to
        self._previous = m[x][y]

        # move the ghost
        m.place_char(x, y, "G")

        # test for ghost-player collision
        if [x, y] == player_location:
            collision = True
        
        return collision
