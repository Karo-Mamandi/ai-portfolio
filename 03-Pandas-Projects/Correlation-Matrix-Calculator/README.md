# Correlation Matrix Calculator

A Python program that computes correlations between academic subjects using Pandas.

## Features

- Creates a dataset with student scores in three subjects
- Calculates correlation matrix between subjects
- Highlights relationships in academic performance
- Demonstrates data analysis capabilities

## How It Works

The program:
1. Creates a Pandas DataFrame with student scores
2. Contains columns: Math, Physics, Chemistry
3. Includes 6 students with varying scores
4. Calculates the correlation matrix
5. Displays the correlations between all subject pairs

## Correlation Explained

Correlation measures the strength and direction of relationships between variables:

- **+1.0**: Perfect positive correlation (both increase together)
- **0**: No correlation (no relationship)
- **-1.0**: Perfect negative correlation (one increases, other decreases)

### Correlation Values Interpretation:
- **0.9 to 1.0**: Very strong positive
- **0.7 to 0.9**: Strong positive
- **0.5 to 0.7**: Moderate positive
- **0.3 to 0.5**: Weak positive
- **0 to 0.3**: Negligible

## Requirements
```
pandas>=1.0.0
```
