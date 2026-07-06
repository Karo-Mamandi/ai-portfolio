# Histogram
# Idea: Show distribution of students' scores in a class.

import matplotlib.pyplot as plt

# Student scores data
scores = [55,60,65,70,72,75,80,82,85,90,92,95,100]

# Create histogram with 5 bins
plt.hist(scores, bins=5, color='orange', edgecolor='black')

# Add labels and title
plt.title("Score Distribution")
plt.xlabel("Score Range")
plt.ylabel("Frequency")

# Display the chart
plt.show()
