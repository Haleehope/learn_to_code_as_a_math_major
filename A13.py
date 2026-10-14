# ###################################################################
# Make an ASCII topographic map
# ###################################################################

# import the random library
import random

# create a function that returns the elevation symbol given a height
def elevation_symbol(height):
    if height < 25:
        return "."
    elif height < 50:
        return "-"
    elif height < 75:
        return "^"
    else:
        return "A"

# start by creating a small 8x8 map
SIZE = 8

# generate random elevations between 0 and 100
# we'll do this by nesting lists inside of a larger list
elevations = []
for row in range(SIZE):
    new_row = []
    # append a random integer that is the elevation on this map
    for col in range(SIZE):
        new_row.append(random.randint(0, 100))
    elevations.append(new_row)

# print the elevation map with the elevation symbols
print("Topographic map:")
for row in elevations:
    symbols = []
    for height in row:
        symbols.append(elevation_symbol(height))
    print(" ".join(symbols))

# find the highest point
# one of the best ways to find a maximum is loop through the list and set the maximum to max(current_max, next_number)
# but what do we set as the current_max for the first element in the list? 
# we usually set this to an impossible minimum (say -1 or -infinity)
highest = -1
highest_position = None

# loop through the map
for row in range(SIZE):
    for col in range(SIZE):
        # if the height is greater than the current maximum, set that to the new maximum and store its position on the map
        height = elevations[row][col]
        if height > highest:
            highest = height
            highest_position = (row, col)

# print the highest point and its position
print(f"\nHighest elevation: {highest}")
print(f"Position: {highest_position}")