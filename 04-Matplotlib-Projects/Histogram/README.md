# Histogram - Score Distribution

A Python program that visualizes the distribution of students' scores using a histogram with Matplotlib.

## Features

- Creates a dataset with student scores
- Generates a histogram visualization
- Groups scores into intervals (bins)
- Shows frequency distribution of scores

## How It Works

The program:
1. Creates a list of student scores
2. Uses Matplotlib to create a histogram
3. Divides scores into 5 bins (intervals)
4. Counts how many scores fall into each bin
5. Displays the distribution with bars

## Histogram Explained

A histogram shows the frequency distribution of numerical data:

**Example with 5 bins (scores 55-100):**
- Bin 1: 55-64 (1 student)
- Bin 2: 65-73 (4 students)
- Bin 3: 74-82 (2 students)
- Bin 4: 83-91 (3 students)
- Bin 5: 92-100 (3 students)

## Plotting Parameters Explained

```python
plt.hist(
    scores,           # Data values
    bins=5,           # Number of intervals
    color='orange',   # Bar color
    edgecolor='black' # Bar border color
)
```

## Common Histogram Customizations

```python
# Custom bin edges
bins = [50, 60, 70, 80, 90, 100]
plt.hist(scores, bins=bins)

# More bins for detailed view
plt.hist(scores, bins=10)

# Fewer bins for general view
plt.hist(scores, bins=3)

# Horizontal histogram
plt.hist(scores, bins=5, orientation='horizontal')

# Density (probability) histogram
plt.hist(scores, bins=5, density=True)

# Cumulative histogram
plt.hist(scores, bins=5, cumulative=True)

# Transparent bars
plt.hist(scores, bins=5, alpha=0.7)
```

## Multiple Histograms

```python
# Compare two datasets
plt.hist(class1_scores, bins=5, alpha=0.5, label='Class A')
plt.hist(class2_scores, bins=5, alpha=0.5, label='Class B')
plt.legend()
```

## Requirements
```
matplotlib>=3.0.0
```
