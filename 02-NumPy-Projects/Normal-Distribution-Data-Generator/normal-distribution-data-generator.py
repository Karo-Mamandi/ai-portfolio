# Normal Distribution Data
# Idea: Generate samples from a normal distribution and analyze mean and standard deviation.
# A core concept in statistics and probability.

import numpy as np

# Generate 1000 samples from normal distribution
# loc=0: mean, scale=1: standard deviation, size=1000: number of samples
normal_data = np.random.normal(loc=0, scale=1, size=1000)

# Calculate and display statistical measures
print("Mean:", np.mean(normal_data))          # Average of the samples
print("Standard Deviation:", np.std(normal_data))  # Spread of the samples
