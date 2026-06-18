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
