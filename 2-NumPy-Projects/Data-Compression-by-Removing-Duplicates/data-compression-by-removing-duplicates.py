# Data compression by removing duplicates
# Idea: Remove duplicate values from an array and display the count of each value.

import numpy as np

# Generate 30 random integers between 1 and 10
data = np.random.randint(1, 10, size=30)

# Find unique values and count occurrences of each
unique, counts = np.unique(data, return_counts=True)

# Display the results
print("Data: ", data)
print("Unique values:", unique)
print("Number of each value:", counts)
