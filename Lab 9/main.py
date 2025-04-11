'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/04/10
Description: This project lets users play a game of Pacman across a 10x10 grid. Using console inputs, the player must
try to eat all the food while avoiding the Pacman that will try to eat them.
'''

import maze
import player
import ghost

def main():
    # initialize maze, player, and ghost, and game state
    m = maze.Maze()
    p = player.Player()
    g = ghost.Ghost()
    game = True

    while game:
        # initialize main game loop
        print(m)
        player_move = input("Move (WASD): ").lower()
        while player_move !="w" and player_move !="a" and player_move !="s" and player_move !="d":
            player_move = input("Please enter a valid input. Move (WASD): ").lower()

        player_hit = p.move(player_move)
        ghost_hit = g.move()

        # player loss: player collides with ghost
        if player_hit or ghost_hit:
            print(m)
            print("You ghost caught you! Game over...")
            break

        # player win: dot count reaches 0
        if m.count_dots() == 0:
            print("All dots eaten. You win!")
            break
        
# execute main game
if __name__ == "__main__":
    main()
