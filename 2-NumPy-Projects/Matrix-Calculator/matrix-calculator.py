# Matrix Calculator
# Idea: A simple tool for basic matrix operations such as addition, multiplication, and determinant calculation.
# creat as a foundation for larger linear algebra projects.

import numpy as np

# Create two 2x2 matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 3]])

# Display the first matrix
print(f"First matrices: \n {A}")

# Display the second matrix
print(f"Second matrices: \n {B}")

# Perform and display basic matrix operations
print("Addition:\n", A + B)           # Element-wise addition
print("Subtraction:\n", A - B)        # Element-wise subtraction
print("Matrix Multiplication:\n", A @ B)  # Matrix multiplication using @ operator
print("Determinant of A:", np.linalg.det(A))  # Calculate determinant
