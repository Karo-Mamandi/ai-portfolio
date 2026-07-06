# Subplots
# Idea: Display sales of two products in separate charts.

import matplotlib.pyplot as plt

# Data for the charts
x = [1,2,3,4,5]           # X-axis data
y1 = [10,20,30,40,50]     # Product A sales
y2 = [5,15,25,35,45]      # Product B sales

# Create first subplot (position 1 in 1x2 grid)
plt.subplot(1,2,1)
plt.plot(x,y1)
plt.title("Product A")

# Create second subplot (position 2 in 1x2 grid)
plt.subplot(1,2,2)
plt.plot(x,y2)
plt.title("Product B")

# Display both charts
plt.show()
