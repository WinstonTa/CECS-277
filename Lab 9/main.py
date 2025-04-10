import random
import maze
import player
import ghost

def main():

    m = maze.Maze()
    p = player.Player()
    g = ghost.Ghost()
    
    game = True

    while game == True:
        print(m)
        player_move = input("Move (WASD): ").lower()
        p.move(player_move)
        g.move()
    

if __name__ == "__main__":
    main()