import random
import numpy as np

def start_game():
    # Create an empty grid (4x4 matrix)
    mat = np.zeros((4, 4), dtype=int)

    # Printing controls for the user
    print("Moving Instructions:")
    print("'W' or 'w': Move Up")
    print("'S' or 's': Move Down")
    print("'A' or 'a': Move Left")
    print("'D' or 'd': Move Right")

    # Calling the function to add a new 2 in the grid after initialization
    add_new_2(mat)
    return mat

# Function to add a new 2 in the grid at any random empty cell
def add_new_2(mat):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        mat[r][c] = 2

# Function to get the current state of the game
def get_current_state(mat):
    if 2048 in mat:
        return 'WON'
    elif 0 in mat:
        return 'GAME NOT OVER'
    else:
        for i in range(4):
            for j in range(3):
                if mat[i][j] == mat[i][j + 1] or mat[j][i] == mat[j + 1][i]:
                    return 'GAME NOT OVER'
        return 'LOST'

# Function to compress the grid after every step before and after merging cells
def compress(mat):
    new_mat = np.zeros((4, 4), dtype=int)
    changed = False

    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1

    return new_mat, changed

# Function to merge the cells in the matrix after compressing
def merge(mat):
    changed = False

    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
                changed = True

    return mat, changed

# Function to move left
def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, _ = compress(new_grid)
    return new_grid, changed

# Function to move right
def move_right(grid):
    new_grid = np.flip(grid, axis=1)
    new_grid, changed = move_left(new_grid)
    new_grid = np.flip(new_grid, axis=1)
    return new_grid, changed

# Function to move up
def move_up(grid):
    new_grid = np.transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = np.transpose(new_grid)
    return new_grid, changed

# Function to move down
def move_down(grid):
    new_grid = np.transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = np.transpose(new_grid)
    return new_grid, changed

# Driver code
if __name__ == '__main__':
    mat = start_game()

while True:
    x = input("Press the command: ")

    if x.lower() == 'w':
        mat, flag = move_up(mat)
    elif x.lower() == 's':
        mat, flag = move_down(mat)
    elif x.lower() == 'a':
        mat, flag = move_left(mat)
    elif x.lower() == 'd':
        mat, flag = move_right(mat)
    else:
        print("Invalid Key Pressed")
        continue

    status = get_current_state(mat)
    for row in mat:
        print(row)

    if status == 'GAME NOT OVER':
        add_new_2(mat)
    else:
        print("Game Over!")
        break
