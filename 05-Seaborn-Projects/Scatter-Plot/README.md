# Seaborn Scatter Plot - Total Bill vs Tip

A Python program that creates a scatter plot to visualize the relationship between total bill and tip amounts using Seaborn.

## Features

- Loads the restaurant tips dataset from Seaborn
- Creates a scatter plot of total bill vs tip
- Colors points by gender (sex)
- Shows relationship between two continuous variables
- Customizes labels and legend

## How It Works

The program:
1. Loads the built-in tips dataset
2. Creates a scatter plot with total_bill on x-axis and tip on y-axis
3. Colors data points by sex (Male/Female)
4. Adds descriptive labels and title
5. Customizes the legend

## Scatter Plot Explained

A scatter plot displays values for two variables:
- **X-axis**: Total bill amount ($)
- **Y-axis**: Tip amount ($)
- **Color**: Gender of the customer
- **Pattern**: Shows if higher bills lead to higher tips

## Plotting Parameters Explained

```python
sns.scatterplot(
    x="total_bill",    # X-axis variable
    y="tip",           # Y-axis variable
    data=df,           # Data source
    hue="sex"          # Color by gender
)
```

## Requirements
```
seaborn>=0.11.0
matplotlib>=3.0.0
```
