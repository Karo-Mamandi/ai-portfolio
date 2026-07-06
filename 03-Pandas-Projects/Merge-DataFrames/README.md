# Merge DataFrames with Pandas

A Python program that merges student scores with class information using Pandas. Demonstrates relational data handling and joining operations.

## Features

- Creates two separate DataFrames with student data
- Merges DataFrames on a common key (Name)
- Combines student scores with subject grades
- Demonstrates relational database concepts

## How It Works

The program:
1. Creates a DataFrame with student names and scores
2. Creates a DataFrame with student names and subject grades (Math, Physics, Chemistry)
3. Merges both DataFrames using the "Name" column as the key
4. Combines all data into a single DataFrame
5. Displays the merged results

## Merge Operations Explained

The `merge()` function combines two DataFrames based on a common column:

**How it Works:**
1. Identifies the key column ("Name")
2. Matches rows with the same key in both DataFrames
3. Combines all columns from both DataFrames
4. Creates a new unified DataFrame

## Types of Joins

```python
# Inner Join (default): Only matching keys
merged = pd.merge(df1, df2, on="Key")

# Left Join: Keep all rows from left DataFrame
merged = pd.merge(df1, df2, on="Key", how="left")

# Right Join: Keep all rows from right DataFrame
merged = pd.merge(df1, df2, on="Key", how="right")

# Outer Join: Keep all rows from both DataFrames
merged = pd.merge(df1, df2, on="Key", how="outer")
