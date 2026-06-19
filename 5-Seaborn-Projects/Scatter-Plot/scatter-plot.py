# Seaborn Scatter Plot
# Visualizes relationship between two continuous variables

import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
df = sns.load_dataset("tips")

# Create scatter plot: total_bill vs tip, colored by sex
sns.scatterplot(x="total_bill", y="tip", data=df, hue="sex")

# Add title
plt.title("Total Bill vs Tip by Sex")

# Add labels for clarity
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")

# Add legend with custom title
plt.legend(title="Sex")

# Display the plot
plt.show()
