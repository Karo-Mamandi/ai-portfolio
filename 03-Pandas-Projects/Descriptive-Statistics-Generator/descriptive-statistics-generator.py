# Descriptive Statistics 
# Idea: Generate descriptive statistics (mean, min, max, quartiles). A quick way to summarize datasets.

import pandas as pd

# Create a DataFrame with student scores
students = pd.DataFrame({
    "Score": [18.7, 14.3, 19.1, 16.7, 20, 14.6, 18.3, 17.1, 16.8, 19.5, 14.6, 11.2]
})

# Generate and display descriptive statistics
print("Descriptive Statistics:\n", students.describe())
