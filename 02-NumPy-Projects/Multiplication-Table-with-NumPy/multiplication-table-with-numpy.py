# Simulating a multiplication table with NumPy
# Idea: Build a multiplication table from 1 to 10 using broadcasting.

import numpy as np

# Create array of numbers 1 to 10
x = np.arange(1, 11)

# Multiply column vector (x[:, None]) with row vector (x)
# Broadcasting creates the entire multiplication table
table = x[:, None] * x

# Display the multiplication table
print("about Multiplication 1 to 10: ")
print(table)
