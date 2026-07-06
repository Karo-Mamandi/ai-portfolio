# Student Dataset
# Create a dataset of students and calculate average scores. Useful for basic educational data analysis.

import pandas as pd

# Create a DataFrame with student information
students = pd.DataFrame({
    "Name": ["Karo", "Ali", "Daniel", "Aria", "Amir"],  # Student names
    "Age": [19, 22, 18, 19, 21],                        # Student ages
    "Score": [19.4, 15.7, 17.8, 18.1, 17.9]             # Student scores
})

# Calculate and display the average score
print("Average Score:", students["Score"].mean())
