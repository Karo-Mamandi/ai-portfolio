# Colored Bar Chart
# Idea: Display monthly income with custom colors.

import matplotlib.pyplot as plt

# Data for the chart
months = ["Jan","Feb","Mar","Apr","May"]           # Month names
income = [200, 250, 300, 280, 350]                 # Income values

# Create bar chart with custom hexadecimal colors
plt.bar(months, income, color=['#FF5733','#33FF57','#3357FF','#FF33A6','#FFD433'])

# Add title
plt.title("Monthly Income")

# Display the chart
plt.show()
  
