# Seaborn KDE Plot
# Visualizes probability density of a numerical variable

import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
df = sns.load_dataset("tips")

# Create KDE plot of total bill by gender
sns.kdeplot(x="total_bill", data=df, hue="sex", fill=True)

# Add title
plt.title("Total Bill Density by Gender")

# Display the plot
plt.show()
