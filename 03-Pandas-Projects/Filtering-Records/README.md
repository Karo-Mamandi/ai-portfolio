# Filtering Records with Pandas

A Python program that filters student records based on score thresholds using Pandas.

## Features

- Creates a student dataset with names and scores
- Filters students based on score condition
- Extracts meaningful subsets of data
- Demonstrates boolean indexing in Pandas

## How It Works

The program:
1. Creates a DataFrame with student names and scores
2. Applies a filter condition (Score > 18)
3. Creates a boolean mask to identify matching rows
4. Returns only the rows that meet the condition
5. Displays the filtered results

## Filtering Explained

Boolean indexing in Pandas:
1. **Condition**: `students["Score"] > 18` creates a boolean series
2. **Mask**: Returns True/False for each row
3. **Selection**: `students[mask]` keeps only True rows

## Common Filtering Examples

```python
# Score greater than 18
students[students["Score"] > 18]

# Score less than 16
students[students["Score"] < 16]

# Score between 16 and 18
students[(students["Score"] >= 16) & (students["Score"] <= 18)]

# Name equals "Ali"
students[students["Name"] == "Ali"]
