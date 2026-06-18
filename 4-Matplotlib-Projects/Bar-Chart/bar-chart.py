# Bar Chart
# Idea: Compare sales of three products.

import matplotlib.pyplot as plt

# Data for the chart
products = ["A","B","C"]           # Product names
sales = [50, 70, 40]               # Sales figures

# Create bar chart with different colors
plt.bar(products, sales, color=['red','green','blue'])

# Add labels and title
plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

# Display the chart
plt.show()
