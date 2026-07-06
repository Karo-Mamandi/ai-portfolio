# Data Filtering with NumPy

A Python program that filters numerical data using boolean indexing in NumPy.

## Features

- Filters array elements based on a condition
- Uses boolean indexing for efficient filtering
- Demonstrates NumPy's powerful array manipulation capabilities

## How It Works

The program:
1. Creates a dataset of numbers
2. Applies a filter condition (values greater than 40)
3. Displays only the filtered results

## Boolean Indexing Explained

Boolean indexing allows you to select elements from an array that satisfy a condition:
```python
data > 40  # Creates a boolean mask: [False, True, True, False, True, False]
data[data > 40]  # Selects only elements where mask is True
```
## Requirements
```
numpy>=1.15.0
```
