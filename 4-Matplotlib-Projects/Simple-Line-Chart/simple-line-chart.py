# Simple Line Chart
# Idea: Show temperature changes over a week.

import matplotlib.pyplot as plt

# Data for the chart
days = ["Sat","Sun","Mon","Tue","Wed","Thu","Fri"]  # Days of the week
temp = [20, 22, 21, 19, 23, 25, 24]                 # Temperatures in Celsius

# Create line chart with markers
plt.plot(days, temp, marker='o')

# Add labels and title
plt.title("Weekly Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")

# Display the chart
plt.show()
