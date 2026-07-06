# Line Chart with Grid - Population Growth

A Python program that visualizes population growth over years with grid lines using Matplotlib.

## Features

- Creates a dataset with years and population figures
- Generates a line chart with markers
- Adds grid lines for better readability
- Shows population growth trend over time

## How It Works

The program:
1. Creates lists for years and population data
2. Uses Matplotlib to create a line chart
3. Adds markers at each data point
4. Enables grid lines on the chart
5. Labels the axes and adds a title
6. Displays the visualization

## Grid Parameters Explained

```python
plt.grid(True)  # Basic grid

# Custom grid options
plt.grid(
    True,               # Show grid
    linestyle='--',     # Dashed lines
    color='gray',       # Grid color
    alpha=0.7,          # Transparency
    axis='both'         # Show on both axes
)
```

## Grid Customization Options

```python
# Custom grid styles
plt.grid(linestyle='-', linewidth=1, color='lightgray')
plt.grid(linestyle='--', linewidth=0.5, color='gray')
plt.grid(linestyle=':', linewidth=1, color='darkgray')

# Grid on specific axis only
plt.grid(axis='x')      # Only vertical lines
plt.grid(axis='y')      # Only horizontal lines
plt.grid(axis='both')   # Both axes (default)

# Major and minor grids
plt.grid(True, which='major', linestyle='-', color='black')
plt.grid(True, which='minor', linestyle=':', color='gray')
plt.minorticks_on()
```

## Complete Customization

```python
# Full grid customization example
plt.plot(years, population, marker='o', markersize=8)
plt.title("Population Growth", fontsize=14, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Population (Million)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7, color='gray')
plt.tick_params(axis='both', labelsize=10)
plt.show()
```

## Requirements
```
matplotlib>=3.0.0
```
