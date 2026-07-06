# Merge Two DataFrames
# Idea: Merge student scores with class information. Demonstrates relational data handling with Pandas.

import pandas as pd

# Create first DataFrame with student names and scores
students = pd.DataFrame({
    "Name": ["Karo", "Ali", "Daniel", "Aria", "Amir"],   # Student names
    "Score": [19.4, 15.7, 17.8, 18.1, 17.9]              # Student scores
})

# Create second DataFrame with student subject grades
classes = pd.DataFrame({
    "Name": ["Karo", "Ali", "Daniel", "Aria", "Amir"],   # Student names
    "Math": [18.2, 14.4, 13.2, 18.8, 16.4],              # Math grades
    "Physics": [15.2, 16.3, 14.7, 18.6, 17.2],           # Physics grades
    "Chemistry": [17.3, 13.4, 18.5, 15.7, 19.6]          # Chemistry grades
})

# Merge both DataFrames on the "Name" column
merged = pd.merge(students, classes, on="Name")

# Display the merged result
print("Merged Data:\n", merged)
