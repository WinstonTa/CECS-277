'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/04/10
Description: This project lets users play a game of Pacman across a 10x10 grid. Using console inputs, the player must
try to eat all the food while avoiding the Pacman that will try to eat them.
'''

import random
import maze
import player
import ghost

def main():

    m = maze.Maze()
    p = player.Player()
    g = ghost.Ghost()

    print(m._m)
    

if __name__ == "__main__":
    main()