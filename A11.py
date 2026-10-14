# ###################################################################
# Build a Minesweeper-style grid
# ###################################################################

# this is great to get you started on a matrix-like problem in Python
# it'll get you used to indexing a matrix in Python if the matrix is just nested lists

# import random to randomly place the mines
import random

# the size of the grid is 5 x 5 and we will place 5 mines
SIZE = 5
NUM_MINES = 5

# create a 5x5 grid of empty cells
grid = []
for row in range(SIZE):
    grid.append(["."] * SIZE) # [.]*SIZE = ['.', '.', '.', '.', '.']

# initialize the number of place mines to be zero
mines_placed = 0

# use a while loop here because it could randomly pick the same row/column combination twice
while mines_placed < NUM_MINES:
    # pick a random row and column, and change the . to a *
    row = random.randint(0, SIZE - 1)
    col = random.randint(0, SIZE - 1)
    if grid[row][col] != "*":
        grid[row][col] = "*"
        mines_placed += 1

# print the grid using .join() to join on the rows
for row in grid:
    print(" ".join(row))

# for each non-mine cell, calculate how many mines are in its 8 neighboring cells
# use a double for loop to loop over the rows and columns
for row in range(SIZE):
    for col in range(SIZE):
        # if the cell is a mine, continue
        if grid[row][col] == "*":
            continue

        # else it is not a mine cell, and we will count how many mines are in it's 8 neighoring cells
        count = 0
        # this is just one way of doing this
        # you could've instead done a lot of if statements in a row (which is what I imagine you did if you're learning how to code)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                neighbor_row = row + dr
                neighbor_col = col + dc

                if 0 <= neighbor_row < SIZE and 0 <= neighbor_col < SIZE:
                    if grid[neighbor_row][neighbor_col] == "*":
                        count += 1
        
        # change that grid cell to be its count of neighboring mines
        # you could've also made a new grid to store these counts; either way is fine
        grid[row][col] = str(count)

# print the grid after finding the count of mines in the 8 neighboring cells using .join() to join on the rows
# I will print a newline first to make the output prettier
print()
for row in grid:
    print(" ".join(row))
