# Subplots - Multiple Product Sales Charts

A Python program that displays sales of two products in separate charts using Matplotlib subplots.

## Features

- Creates two separate charts in one figure
- Shows sales data for Product A and Product B
- Demonstrates subplot layout configuration
- Enables side-by-side comparison

## How It Works

The program:
1. Creates data for x-axis and two products
2. Uses `subplot()` to divide the figure into multiple plots
3. Plots Product A in the first chart
4. Plots Product B in the second chart
5. Adds titles to each chart
6. Displays both charts side by side

## Subplot Layout Explained

```python
plt.subplot(rows, columns, index)
```

## Parameters:

    rows: Number of rows in the grid (1)

    columns: Number of columns in the grid (2)

    index: Position of the current plot (1 or 2)

## Layout Visualization:
```python
[Position 1] [Position 2]
```

  ## Common Subplot Layouts

  ```python
# 1 row, 2 columns (side by side)
plt.subplot(1,2,1)  # Left chart
plt.subplot(1,2,2)  # Right chart

# 2 rows, 1 column (stacked)
plt.subplot(2,1,1)  # Top chart
plt.subplot(2,1,2)  # Bottom chart

# 2 rows, 2 columns (2x2 grid)
plt.subplot(2,2,1)  # Top-left
plt.subplot(2,2,2)  # Top-right
plt.subplot(2,2,3)  # Bottom-left
plt.subplot(2,2,4)  # Bottom-right

# 2 rows, 3 columns (2x3 grid)
plt.subplot(2,3,1)  # Position 1
plt.subplot(2,3,2)  # Position 2
# ... up to position 6
```

## Using plt.subplots() (Recommended)

```python
# Modern approach with more control
fig, axes = plt.subplots(1, 2)  # 1 row, 2 columns
axes[0].plot(x, y1)
axes[0].set_title("Product A")
axes[1].plot(x, y2)
axes[1].set_title("Product B")
plt.tight_layout()
plt.show()
```

## Multiple Chart Types

```python
# Different charts in subplots
plt.subplot(1,2,1)
plt.bar(x, y1)  # Bar chart

plt.subplot(1,2,2)
plt.scatter(x, y2)  # Scatter plot
```

## Requirement
```
matplotlib>=3.0.0
```
