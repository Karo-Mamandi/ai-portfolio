# Line Chart with Grid
# Idea: Show population growth over years with grid lines.

import matplotlib.pyplot as plt

# Data for the chart
years = [2000,2005,2010,2015,2020]           # Years
population = [2.5, 2.7, 3.0, 3.3, 3.6]       # Population in millions

# Create line chart with markers
plt.plot(years, population, marker='o')

# Add labels and title
plt.title("Population Growth")
plt.xlabel("Year")
plt.ylabel("Population (Million)")

# Add grid lines for better readability
plt.grid(True)

# Display the chart
plt.show()
