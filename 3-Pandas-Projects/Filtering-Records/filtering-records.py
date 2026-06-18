# Filtering Records
# Idea: Filter students based on score thresholds. Shows how Pandas can extract meaningful subsets of data.

import pandas as pd

# Create a DataFrame with student information
students = pd.DataFrame({
    "Name": ["Karo", "Ali", "Daniel", "Aria", "Amir"],  # Student names
    "Score": [19.4, 15.7, 17.8, 18.1, 18.1]            # Student scores
})

# Filter and display students with score greater than 18
print("Students with Score > 18:\n", students[students["Score"] > 18])
