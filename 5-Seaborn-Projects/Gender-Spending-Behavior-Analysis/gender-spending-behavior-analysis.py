# Use Case: Used to compare spending behavior between different genders and identify potential differences in customer payments.

import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in restaurant tips dataset
df = sns.load_dataset("tips")

# Create boxplot comparing total bill by gender
sns.boxplot(x="sex", y="total_bill", data=df)

# Add title to the plot
plt.title("Total Bill Comparison by Gender")

# Display the plot
plt.show()
