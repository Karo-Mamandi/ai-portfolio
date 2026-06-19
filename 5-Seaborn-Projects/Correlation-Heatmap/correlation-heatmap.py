# Use Case: Commonly used in data science and machine learning to identify relationships between numerical features and reduce multicollinearity.

import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in iris dataset
df = sns.load_dataset("iris")

# Compute correlation matrix for numerical columns only
correlation_matrix = df.corr(numeric_only=True)

# Create heatmap with correlation values and color scheme
sns.heatmap(
    correlation_matrix,
    annot=True,           # Show correlation values in cells
    cmap="coolwarm"       # Color scheme for correlation strength
)

# Add title to the plot
plt.title("Correlation Heatmap")

# Display the plot
plt.show()
