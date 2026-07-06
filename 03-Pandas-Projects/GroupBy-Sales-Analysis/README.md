# GroupBy Sales Analysis

A Python program that demonstrates data aggregation by grouping sales data by day and calculating totals using Pandas.

## Features

- Creates a sales dataset with day and amount columns
- Groups data by day of the week
- Calculates total sales for each day
- Demonstrates practical business analytics

## How It Works

The program:
1. Creates a DataFrame with sales transactions
2. Contains columns: Day (day of week) and Amount (sale value)
3. Groups data by the "Day" column
4. Calculates the sum of "Amount" for each group
5. Displays total sales per day

## GroupBy Explained

The `groupby()` operation splits data into groups based on a column, then applies an aggregation function:

**Process:**
1. **Split**: Data is divided into groups (Mon, Tue)
2. **Apply**: Aggregate function (sum) is applied to each group
3. **Combine**: Results are combined into a new DataFrame

## Common Aggregation Functions

- `sum()`: Total of values
- `mean()`: Average of values
- `count()`: Number of values
- `max()`: Maximum value
- `min()`: Minimum value
- `std()`: Standard deviation
