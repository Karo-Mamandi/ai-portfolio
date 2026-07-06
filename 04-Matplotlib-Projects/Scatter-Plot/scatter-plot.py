# Scatter Plot
# Idea: Show relationship between height and weight of people.

import matplotlib.pyplot as plt

# Data for the chart
height = [160, 165, 170, 175, 180, 185, 190, 195]  # Heights in cm
weight = [55, 60, 65, 70, 75, 80, 85, 90]          # Weights in kg

# Create scatter plot with purple points
plt.scatter(height, weight, color='purple')

# Add labels and title
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")

# Display the chart
plt.show()
