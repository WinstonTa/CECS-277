import maze

class Player:

    def move(self, direction: str) -> bool:
        """
        Player is allowed to move in desired direction.

        Args:
            direction (str): inputs WASD corresponding to up, left, down, and right respectively

        Returns:
            A boolean that returns True if the player collided into the ghost, False if the player is safe.
        """

        # initalize maze and player location
        m = maze.Maze()
        player_location = m.search_maze("P")
        x = player_location[0]
        y = player_location[1]

        # update player location depending on input
        m.place_char(x, y, " ")

        if direction == "w":
            x -= 1
        elif direction == "s":
            x += 1
        elif direction == "a":
            y -= 1
        elif direction == "d":
            y += 1

        # check that player did not run into wall and update new location to "P"  
        if not m.is_wall(x, y):
            if m[x][y] == "G":
                return True
            m.place_char(x, y, "P")
        else:
            # undo move by replacing the player back if hit wall
            m.place_char(player_location[0], player_location[1], "P")
        
        # check if player ran into ghost
        if m.search_maze("G") == m.search_maze("P"):
            return True
        
        return False
