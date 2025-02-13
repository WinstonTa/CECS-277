import random

ship_lc = [random.randint(0,3),random.randint(0,3)]    # ship top left corner
ship_rc = [ship_lc[0],ship_lc[1]+1]                    # ship top right corner
ship_bl = [ship_lc[0]+1,ship_lc[1]]                    # ship bottom left corner
ship_rl = [ship_lc[0]+1,ship_lc[1]+1]                  # ship bottom right corner

print(ship_lc)
print(ship_rc)
print(ship_bl)
print(ship_rl)

print('  1 2 3 4 5')
alpha = ['A','B','C','D','E']
solution_grid = [[],[],[],[],[]]
for i in range(5):                      # rows
    solution_grid[i].append(alpha[i])
    for j in range(5):                  # columns
        if [i,j] == ship_lc or [i,j] == ship_rc or \
             [i,j] == ship_bl or [i,j] == ship_rl :
            solution_grid[j].append('*')
        else:
            solution_grid[j].append('~')
    #solution_grid[i].append(' ')

print(solution_grid)

for i in range(5):
    for j in range(6):
        print(solution_grid[i][j], end = ' ')
    print()


'''
# regular game board print
for i in range(5):
    print(alpha[i], end=' ')
    for j in range(5):
      print('~', end = ' ')
    print()'''