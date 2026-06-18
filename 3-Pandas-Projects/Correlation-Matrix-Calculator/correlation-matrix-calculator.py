# Correlation Matrix
# Idea: Compute correlations between subjects (Math, Physics, Chemistry). Highlights relationships in academic performance.

import pandas as pd

# Create a DataFrame with student scores in three subjects
students = pd.DataFrame({
    "Math": [18.2, 14.4, 13.2, 18.8, 16.4, 17.1],
    "Physics": [15.2, 16.3, 14.7, 18.6, 17.2, 11.3],
    "Chemistry": [17.3, 13.4, 18.5, 15.7, 19.6, 18.9]
})

# Calculate and display correlation matrix
print("Correlation:\n", students.corr())
