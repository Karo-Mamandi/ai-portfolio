# Descriptive Statistics Generator

A Python program that generates descriptive statistics for a dataset using Pandas.

## Features

- Creates a dataset with student scores
- Calculates comprehensive descriptive statistics
- Provides a quick summary of the data
- Includes mean, min, max, quartiles, and more

## How It Works

The program:
1. Creates a DataFrame with student scores
2. Uses Pandas `describe()` method
3. Generates statistical summary including:
   - Count (number of values)
   - Mean (average)
   - Standard Deviation (spread)
   - Minimum value
   - 25th Percentile (Q1)
   - 50th Percentile (Median / Q2)
   - 75th Percentile (Q3)
   - Maximum value

## Descriptive Statistics Explained

**Key Measures:**
- **Count**: Number of data points
- **Mean**: Average value
- **Std**: Standard deviation (measure of spread)
- **Min**: Smallest value
- **25%**: First quartile (25% of data below this)
- **50%**: Median (middle value)
- **75%**: Third quartile (75% of data below this)
- **Max**: Largest value

## Common Aggregation Functions

- `mean()`: Calculate average
- `median()`: Find middle value
- `mode()`: Most frequent value
- `std()`: Standard deviation
- `var()`: Variance
- `min()`: Minimum value
- `max()`: Maximum value
- `quantile()`: Percentile values

## Requirements
```
pandas>=1.0.0
```
