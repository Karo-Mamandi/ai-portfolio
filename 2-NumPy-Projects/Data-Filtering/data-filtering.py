import numpy as np

# Create a sample dataset
data = np.array([12, 45, 67, 23, 89, 34])

# Filter: Keep only numbers greater than 40
filtered = data[data > 40]

# Display the filtered results
print("Numbers greater than 40:", filtered)
