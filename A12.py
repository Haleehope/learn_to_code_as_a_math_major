# ###################################################################
# Simulate a random walk
# ###################################################################

# import the random and math libraries
import random
import math

# create a function that will randomly move you one unit north, south, east, or west
def random_walk(steps):
    # start at (0, 0)
    x = 0
    y = 0

    # for 0 to steps-1, move one unit in a random direction using random.choice()
    for step in range(steps):
        direction = random.choice(["north", "south", "east", "west"])

        if direction == "north":
            y += 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        elif direction == "west":
            x -= 1

    # use the l2 norm to find the distance from (0, 0)
    distance = math.sqrt(x**2 + y**2)

    # return the l2 distance
    return x, y, distance


# call the function to generate a random walk with 100 steps
x, y, distance = random_walk(100)

# print your final position and the distance from (0, 0)
print(f"Final position: ({x}, {y})")
print(f"Distance from origin: {distance:.2f}")

# Simulate 1000 walks and give the average distance after 100 steps
distances = []

for i in range(1000):
    x, y, distance = random_walk(100)
    distances.append(distance)

average_distance = sum(distances) / len(distances)

print(f"Average distance after 100 steps: {average_distance:.2f}")
