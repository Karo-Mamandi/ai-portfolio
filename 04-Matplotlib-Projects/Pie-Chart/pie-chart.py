# Pie Chart
# Idea: Display market share of three companies.

import matplotlib.pyplot as plt

# Data for the chart
companies = ["Apple","Samsung","Huawei"]  # Company names
share = [40, 35, 25]                      # Market share percentages

# Create pie chart with percentage labels
plt.pie(share, labels=companies, autopct='%1.1f%%')

# Add title
plt.title("Market Share")

# Display the chart
plt.show()
