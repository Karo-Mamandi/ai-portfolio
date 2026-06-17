import numpy as np

# Sample dataset
data = np.array([10, 20, 30, 40, 50])

# Min-Max normalization to range [0,1]
# Formula: (value - min) / (max - min)
normalized = (data - np.min(data)) / (np.max(data) - np.min(data))

# Display the normalized data
print("Normalized Data:", normalized)
