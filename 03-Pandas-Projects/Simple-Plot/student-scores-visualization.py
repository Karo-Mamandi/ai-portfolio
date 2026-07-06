# Simple Plot
# Idea: Visualize student scores with a bar chart. Shows how Pandas integrates with plotting for data visualization.

import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame with student information
students = pd.DataFrame({
    "Name": ["Karo", "Ali", "Daniel", "Aria", "Amir"],  # Student names
    "Score": [19.4, 15.7, 17.8, 18.1, 17.9]            # Student scores
})

# Create a bar chart showing student scores
students.plot(x="Name", y="Score", kind="bar", title="Student Scores")

# Display the plot
plt.show()
