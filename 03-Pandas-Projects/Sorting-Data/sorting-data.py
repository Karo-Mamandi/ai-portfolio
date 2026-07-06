# Sorting Data
# Idea: Sort student records by score. Demonstrates how Pandas can organize and rank data efficiently.

import pandas as pd

# Create a DataFrame with student information
students = pd.DataFrame({
    "Name": ["Karo", "Ali", "Daniel", "Aria", "Amir"],  # Student names
    "Age": [19, 22, 18, 19, 21],                       # Student ages
    "Score": [19.4, 15.7, 17.8, 18.1, 17.9]            # Student scores
})

# Sort records by Score and display
print("Sorted by Score:\n", students.sort_values("Score"))
