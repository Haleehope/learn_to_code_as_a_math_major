# ###################################################################
# Create your own mountain
# ###################################################################

# import relevant libraries
import numpy as np
import matplotlib.pyplot as plt

# create x and y coordinates
# np.linspace creates essentially a list of evenly spaces integers over an interval
# the three parameters are the starting number, the ending number, and the number of points on the interval
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

# np.meshgrid creates a rectangular coordinate grid from two or more one-dimensional arrays
# each element (X_{ij}, Y_{ij}) forms a coordinate pair on the grid
X, Y = np.meshgrid(x, y)

# create a function that takes in X, Y, their given centers, and the height and width of the surface,
# and returns a list of lists that contains each element (X_{ij}, Y_{ij}) evaluated at the function
def hill(X, Y, center_x, center_y, height, width):
    return height * np.exp(
        -((X - center_x)**2 + (Y - center_y)**2) / width
    )


# First mountain
mountain1 = hill(X, Y, -3, 0, 10, 15)

# Second mountain
mountain2 = hill(X, Y, 4, 3, 7, 10)

# Combine them
Z = mountain1 + mountain2

# Create the 3D plot with matplotlib
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, cmap="terrain")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Elevation")
ax.set_title("My Mountain Range")
plt.show()
