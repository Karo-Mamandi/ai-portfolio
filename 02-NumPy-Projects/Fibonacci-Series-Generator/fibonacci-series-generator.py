# Fibonacci Series
# Idea: Generate the Fibonacci sequence using NumPy arrays.
# A classic example of algorithmic implementation with numerical tools.

import numpy as np

# Create array of 10 zeros
fib = np.zeros(10, dtype=int)

# Set first two values to 1
fib[0:2] = 1

# Generate remaining Fibonacci numbers
for i in range(2, 10):
    fib[i] = fib[i-1] + fib[i-2]  # Sum of two previous numbers

# Display the Fibonacci series
print("Fibonacci Series:", fib)
