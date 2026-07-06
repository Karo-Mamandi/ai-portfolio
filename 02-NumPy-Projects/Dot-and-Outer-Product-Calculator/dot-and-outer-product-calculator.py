# Dot and Outer Product
# Idea: Compute dot and outer products of vectors.
# Essential for understanding vector operations in physics, AI, and machine learning.

import numpy as np

# Create two vectors
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Calculate and display dot product (scalar result)
print("Dot Product:", np.dot(v1, v2))

# Display separator
print("----------")

# Calculate and display outer product (matrix result)
print("Outer Product:\n", np.outer(v1, v2))
