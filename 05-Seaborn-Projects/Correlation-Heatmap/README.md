# Correlation Heatmap - Iris Dataset

A Python program that creates a correlation heatmap to visualize relationships between numerical features using Seaborn and Matplotlib.

## Features

- Loads the classic Iris dataset from Seaborn
- Computes correlation matrix between numerical features
- Creates a heatmap visualization
- Shows correlation values on the heatmap
- Uses color scheme to highlight relationships

## How It Works

The program:
1. Loads the built-in Iris dataset from Seaborn
2. Calculates the correlation matrix for numerical columns
3. Creates a heatmap visualization
4. Displays correlation values on each cell
5. Uses color gradient to show correlation strength

## Dataset Information

The **Iris dataset** contains flower measurements:
- **sepal_length**: Length of sepal (cm)
- **sepal_width**: Width of sepal (cm)
- **petal_length**: Length of petal (cm)
- **petal_width**: Width of petal (cm)
- **species**: Type of iris flower (Setosa, Versicolor, Virginica)

## Correlation Explained

Correlation measures the strength and direction of relationships:

**Values range from -1 to +1:**
- **+1.0**: Perfect positive correlation
- **0**: No correlation
- **-1.0**: Perfect negative correlation

**Interpretation:**
- **0.9 to 1.0**: Very strong
- **0.7 to 0.9**: Strong
- **0.5 to 0.7**: Moderate
- **0.3 to 0.5**: Weak
- **0 to 0.3**: Negligible

## Heatmap Parameters Explained

```python
sns.heatmap(
    correlation_matrix,   # Data to display
    annot=True,           # Show values in cells
    cmap="coolwarm"       # Color scheme
)
```

## Common Color Maps
```python
# Diverging (best for correlations)
cmap="coolwarm"      # Blue-white-red
cmap="RdBu"          # Red-blue
cmap="seismic"       # Red-white-blue

# Sequential (for one-direction data)
cmap="viridis"       # Purple-green-yellow
cmap="plasma"        # Purple-red-yellow
cmap="Blues"         # Light to dark blue

# Other options
cmap="YlOrRd"        # Yellow-orange-red
cmap="Greens"        # Light to dark green
```

## Requirements
```
seaborn>=0.11.0
matplotlib>=3.0.0
```
