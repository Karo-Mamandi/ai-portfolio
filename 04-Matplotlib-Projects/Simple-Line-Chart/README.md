# Simple Line Chart - Weekly Temperature

A Python program that visualizes temperature changes over a week using a line chart with Matplotlib.

## Features

- Creates a dataset with daily temperature readings
- Generates a line chart visualization
- Shows temperature trends over time
- Includes markers for each data point

## How It Works

The program:
1. Creates lists for days of the week and corresponding temperatures
2. Uses Matplotlib to plot a line chart
3. Adds markers at each data point
4. Labels the axes and adds a title
5. Displays the visualization

## Plotting Parameters Explained

```python
plt.plot(
    days,              # x-axis data (days)
    temp,              # y-axis data (temperatures)
    marker='o'         # Marker style for data points
)
```

## Common Marker Styles

>### Circle marker
>```plt.plot(x, y, marker='o')```

>### Square marker
>```plt.plot(x, y, marker='s')```

>### Triangle marker
>```plt.plot(x, y, marker='^')```

>### Diamond marker
>```plt.plot(x, y, marker='D')```

>### Star marker
>```plt.plot(x, y, marker='*')```

>### No marker (line only)
>```plt.plot(x, y)```

## Common Line Styles

>### Solid line (default)
>```plt.plot(x, y, linestyle='-')```

>### Dashed line
>```plt.plot(x, y, linestyle='--')```

>### Dotted line
>```plt.plot(x, y, linestyle=':')```

>### Dash-dot line
>```plt.plot(x, y, linestyle='-.')```

## Requirements
```
matplotlib>=3.0.0
```
