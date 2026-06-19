# Seaborn Line Plot
# Visualizes trends over time or continuous data

import seaborn as sns
import matplotlib.pyplot as plt

# Load the flights dataset
df = sns.load_dataset("flights")

# Aggregate passengers by year
yearly = df.groupby("year")["passengers"].sum().reset_index()

# Create line plot
sns.lineplot(x="year", y="passengers", data=yearly, marker="o")

# Add title
plt.title("Total Passengers by Year")

# Display the plot
plt.show()
