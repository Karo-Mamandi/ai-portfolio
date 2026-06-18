# Bar Chart - Product Sales Comparison

A Python program that visualizes and compares sales of three products using a bar chart with Matplotlib.

## Features

- Creates a dataset with product names and sales figures
- Generates a bar chart visualization
- Uses different colors for each product
- Compares sales performance across products

## How It Works

The program:
1. Creates lists for product names and corresponding sales
2. Uses Matplotlib to create a bar chart
3. Assigns different colors to each bar
4. Labels the axes and adds a title
5. Displays the visualization

## Plotting Parameters Explained

```python
plt.bar(
    products,          # x-axis data (product names)
    sales,             # y-axis data (sales figures)
    color=['red','green','blue']  # Bar colors
)
```

## Common Color Options
```python
# Named colors
color=['red', 'green', 'blue']

# Hex colors
color=['#FF0000', '#00FF00', '#0000FF']

# RGB values
color=[(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)]

# Predefined colormaps
color='skyblue'
color='orange'
```

## Custom Bar Chart Options
```python
# Horizontal bar chart
plt.barh(products, sales)

# Stacked bar chart
plt.bar(x, y1, label='Product A')
plt.bar(x, y2, bottom=y1, label='Product B')

# Grouped bar chart
plt.bar(x - width/2, y1, width=width)
plt.bar(x + width/2, y2, width=width)

# Adding values on bars
for i, v in enumerate(sales):
    plt.text(i, v, str(v), ha='center', va='bottom')
```
