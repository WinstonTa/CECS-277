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
            y -= 1
        elif direction == "s":
            y += 1
        elif direction == "a":
            x -= 1
        elif direction == "d":
            x += 1

        # check that player did not run into wall and update new location to "P"  
        if not m.is_wall():
            m.place_char(x, y, "P")
        if m.is_wall():
            m.place_char(player_location[0], player_location[1], "P")
            
        
        # check if player ran into ghost
        if m.search_maze("G") == m.search_maze("P"):
            return True
        else:
            return False
