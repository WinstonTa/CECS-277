import maze
class Player:

    def move(self, direction):

        # update player location depending on input
        player_location = maze.search_maze("P")
        if direction == "w":
            player_location = " "
            new_location = [player_location[0], player_location[1] + 1]
        elif direction == "s":
            player_location = " "
            new_location = [player_location[0], player_location[1] - 1]
        elif direction == "a":
            player_location = " "
            new_location = [player_location[0] - 1, player_location[1]]
        elif direction == "d":
            player_location = " "
            new_location = [player_location[0] + 1, player_location[1]]

        # check that player did not run into wall and update new location to "P"  
        if new_location == "*":
            new_location = player_location
        elif new_location == ".":
            new_location = "P"
        
        # check if player ran into ghost
        if new_location == maze.search_maze("G"):
            return True
        else:
            return False