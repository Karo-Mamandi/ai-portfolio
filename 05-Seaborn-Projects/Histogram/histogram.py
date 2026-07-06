# Seaborn Histogram
# Visualizes distribution of a single numerical variable

import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
df = sns.load_dataset("tips")

# Create histogram of total bill
sns.histplot(x="total_bill", data=df, bins=20, kde=True)

# Add title
plt.title("Distribution of Total Bill")

# Display the plot
plt.show()
