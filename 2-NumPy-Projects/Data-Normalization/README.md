# Data Normalization

A Python program that normalizes numerical data into the range [0,1] using NumPy.

## Features

- Normalizes data to range [0,1]
- Preserves the relative relationships between values
- Useful for preparing datasets in machine learning and data science

## How It Works

The program:
1. Creates a sample dataset of numbers
2. Applies Min-Max normalization formula
3. Displays the normalized data

## Normalization Formula
normalized = (data - min) / (max - min)


This transforms all values to fall between 0 and 1:
- The minimum value becomes 0
- The maximum value becomes 1
- All other values are scaled proportionally

## Why Normalize?

- **Machine Learning**: Many algorithms perform better with normalized data
- **Feature Scaling**: Prevents features with larger values from dominating
- **Data Consistency**: Makes different datasets comparable
- **Faster Convergence**: Helps optimization algorithms converge faster

## Requirements
```
numpy>=1.15.0
```
