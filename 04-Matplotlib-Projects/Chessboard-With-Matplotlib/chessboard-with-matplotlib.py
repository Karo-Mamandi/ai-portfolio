import matplotlib.pyplot as plt
import numpy as np

# Set step sizes for x and y axes
dx, dy = 0.015, 0.05

# Create arrays from -4 to 4 with the step sizes
x = np.arange(-4.0, 4.0, dx)
y = np.arange(-4.0, 4.0, dy)

# Create 2D grids from the x and y arrays
X, Y = np.meshgrid(x, y)

# Get the min and max values for the plot boundaries
extent = np.min(x), np.max(x), np.min(y), np.max(y)

# Create chess board pattern using modulo 2 (alternating 0s and 1s)
z1 = np.add.outer(range(8), range(8)) % 2

# Display the chess board with black/white colors
plt.imshow(z1, cmap="binary_r", interpolation="nearest", extent=extent, alpha=1)

# Define the mathematical function
def chess(x, y):
    return (1 - x / 2 + x ** 5 + y ** 6) * np.exp(-(x ** 2 + y ** 2))

# Calculate the function values for the grid
z2 = chess(X, Y)

# Overlay the function on the chess board with transparency
plt.imshow(z2, alpha=0.7, interpolation="bilinear", extent=extent)

# Add title and display the plot
plt.title("Chess Board with Python")
plt.show()
