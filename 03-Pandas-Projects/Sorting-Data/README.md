# Sorting Data with Pandas

A Python program that sorts student records by score using Pandas.

## Features

- Creates a DataFrame with student information
- Contains student names, ages, and scores
- Sorts records by score in ascending order
- Demonstrates efficient data organization and ranking

## How It Works

The program:
1. Creates a Pandas DataFrame with student data
2. Contains columns: Name, Age, Score
3. Includes five students with varying scores
4. Sorts the DataFrame by the Score column
5. Displays the sorted results

## Sorting Explained

The `sort_values()` method arranges data in order:
- **Default**: Ascending order (lowest to highest)
- **Parameter**: `ascending=False` for descending order
- Returns a new sorted DataFrame

## Requirements
```
pandas>=1.0.0
```
