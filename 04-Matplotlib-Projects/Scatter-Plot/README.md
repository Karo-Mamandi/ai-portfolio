# Scatter Plot - Height vs Weight Relationship

A Python program that visualizes the relationship between height and weight of people using a scatter plot with Matplotlib.

## Features

- Creates a dataset with height and weight measurements
- Generates a scatter plot visualization
- Shows correlation between two variables
- Identifies patterns and trends in data

## How It Works

The program:
1. Creates lists for height and weight measurements
2. Uses Matplotlib to create a scatter plot
3. Plots each person as a point on the chart
4. Labels the axes and adds a title
5. Displays the visualization

## Scatter Plot Explained

A scatter plot displays values for two variables:
- **X-axis**: Height (independent variable)
- **Y-axis**: Weight (dependent variable)
- **Each point**: Represents one person
- **Pattern**: Shows relationship between variables

## Plotting Parameters Explained

```python
plt.scatter(
    height,            # X-axis data
    weight,            # Y-axis data
    color='purple'     # Point color
)
```

## Common Scatter Plot Customizations

```python
# Different sizes
sizes = [50, 100, 150, 200, 250, 300, 350, 400]
plt.scatter(x, y, s=sizes)

# Different colors
colors = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'pink', 'gray']
plt.scatter(x, y, c=colors)

# Alpha transparency
plt.scatter(x, y, alpha=0.5)

# Size based on values
plt.scatter(x, y, s=weights*10)

# Color based on values
plt.scatter(x, y, c=weights, cmap='viridis')
plt.colorbar()  # Add color bar
```

## Adding Trend Line
```python
# Add linear regression line
import numpy as np
z = np.polyfit(height, weight, 1)
p = np.poly1d(z)
plt.plot(height, p(height), "r--", alpha=0.8)
```

## Requirements
```
matplotlib>=3.0.0
```
