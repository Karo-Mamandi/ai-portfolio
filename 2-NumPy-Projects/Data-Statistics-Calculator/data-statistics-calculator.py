import numpy as np
from collections import Counter

# Predefined dataset of 20 numbers
data = [84, 65, 75, 64, 94, 87, 86, 66, 10, 37, 94, 69, 55, 8, 98, 32, 15, 96, 2, 50]

# Display the data
print("Data:", data)

# Calculate and display all statistical measures
print("Max:", np.max(data))                      # Largest value (Max)
print("Min:", np.min(data))                      # Smallest value (Min)
print("Mean:", np.mean(data))                    # Average value
print("Median:", np.median(data))                # Middle value
mode_result = Counter(data).most_common(1)[0]    # Find most frequent value
print("Mode:", mode_result[0])                   # Display the mode
print("Range:", np.max(data) - np.min(data))     # Max - Min
print("Variance:", np.var(data))                 # Average squared deviation
print("Standard Deviation:", np.std(data))       # Square root of variance
print("Coefficient of Variance:", (np.std(data) / np.mean(data)) * 100, "%")  # Relative variability
