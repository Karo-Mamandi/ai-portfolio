# Colored Bar Chart - Monthly Income

A Python program that visualizes monthly income with custom colors using a bar chart with Matplotlib.

## Features

- Creates a dataset with monthly income figures
- Generates a bar chart with custom colors
- Uses hexadecimal color codes for each bar
- Shows income trends over months

## How It Works

The program:
1. Creates lists for months and corresponding income
2. Uses Matplotlib to create a bar chart
3. Assigns a different color to each bar using hex codes
4. Displays the visualization

## Color Formats Explained

```python
# Hexadecimal colors
color=['#FF5733','#33FF57','#3357FF','#FF33A6','#FFD433']
```

## Common Color Formats

```python
# Named colors
color=['red', 'green', 'blue', 'orange', 'yellow']

# RGB (0-1 range)
color=[(1.0, 0.33, 0.2), (0.2, 1.0, 0.34), ...]

# RGB (0-255 range)
color=[(255, 83, 51), (51, 255, 87), ...]

# Hexadecimal shorthand
color=['#F53', '#3F5', '#35F', '#F3A', '#FD3']

# Matplotlib named colors
color=['tomato', 'limegreen', 'royalblue', 'hotpink', 'gold']
```

## Requirements
```
matplotlib>=3.0.0
```
