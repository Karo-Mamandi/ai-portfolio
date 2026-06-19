# Seaborn Bar Plot
# Visualizes categorical data with bars

import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
df = sns.load_dataset("tips")

# Create bar plot: average tip by day
sns.barplot(x="day", y="tip", data=df, hue="sex")

# Add title
plt.title("Average Tip by Day and Gender")

# Display the plot
plt.show()
