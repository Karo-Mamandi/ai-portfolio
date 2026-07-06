# Simple Plot - Student Scores Visualization

A Python program that visualizes student scores using a bar chart with Pandas and Matplotlib.

## Features

- Creates a dataset with student names and scores
- Generates a bar chart visualization
- Displays student performance graphically
- Demonstrates integration of Pandas with plotting

## How It Works

The program:
1. Creates a DataFrame with student names and scores
2. Uses Pandas `plot()` method to create a bar chart
3. Sets the x-axis to student names and y-axis to scores
4. Adds a title to the chart
5. Displays the visualization

## Plotting Parameters Explained

```python
students.plot(
    x = "Name",        # Column for x-axis
    y = "Score",       # Column for y-axis
    kind = "bar",      # Type of plot (bar chart)
    title = "Student Scores"  # Chart title
)
```
## Common Plot Types:
>### Bar chart
>```df.plot(kind="bar")```

>### Line chart
>```df.plot(kind="line")```

>### Scatter plot
>```df.plot(kind="scatter", x="col1", y="col2")```

>### Histogram
>```df.plot(kind="hist")```

>### Pie chart
>```df.plot(kind="pie", y="column")```
