# Pie Chart - Market Share Visualization

A Python program that visualizes market share of three companies using a pie chart with Matplotlib.

## Features

- Creates a dataset with company names and market share percentages
- Generates a pie chart visualization
- Displays percentage values on each slice
- Shows proportional distribution of market share

## How It Works

The program:
1. Creates lists for company names and their market shares
2. Uses Matplotlib to create a pie chart
3. Adds percentage labels to each slice
4. Adds a title to the chart
5. Displays the visualization

## Plotting Parameters Explained

```python
plt.pie(
    share,                # Data values (sizes of slices)
    labels=companies,     # Labels for each slice
    autopct='%1.1f%%'     # Percentage format (1 decimal place)
)
```

## Common Pie Chart Customizations
```python
# Explode a slice (highlight)
explode = (0.1, 0, 0)  # Explode first slice by 10%
plt.pie(share, labels=companies, explode=explode)

# Custom colors
colors = ['#ff9999', '#66b3ff', '#99ff99']
plt.pie(share, labels=companies, colors=colors)

# Shadow effect
plt.pie(share, labels=companies, shadow=True)

# Starting angle (rotate chart)
plt.pie(share, labels=companies, startangle=90)

# Custom percentage format
autopct='%1.1f%%'   # 1 decimal place: 40.0%
autopct='%1.0f%%'   # No decimals: 40%
autopct='%2.2f%%'   # 2 decimal places: 40.00%
