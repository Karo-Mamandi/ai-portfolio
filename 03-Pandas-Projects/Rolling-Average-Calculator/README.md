# Rolling Average Calculator

A Python program that computes rolling averages for stock prices using Pandas. Useful for financial trend analysis and time-series smoothing.

## Features

- Creates a dataset with stock price data
- Calculates rolling (moving) averages
- Uses a window size of 3 periods
- Demonstrates time-series analysis techniques

## How It Works

The program:
1. Creates a DataFrame with stock price data
2. Applies a rolling window of size 3
3. Calculates the mean for each window
4. Adds the rolling average as a new column
5. Displays the original prices with rolling averages

## Rolling Average Explained

A rolling average (moving average) smooths out short-term fluctuations to reveal longer-term trends:

**Window Size = 3:**
- Row 3: (10 + 12 + 15) / 3 = 12.33
- Row 4: (12 + 15 + 20) / 3 = 15.67
- Row 5: (15 + 20 + 18) / 3 = 17.67
- And so on...

**Important:** First (window-1) rows will have NaN values because there aren't enough data points.

## Common Window Functions

```python
# Rolling mean (average)
df["Rolling_Mean"] = df["Price"].rolling(window=5).mean()

# Rolling sum
df["Rolling_Sum"] = df["Price"].rolling(window=5).sum()

# Rolling max
df["Rolling_Max"] = df["Price"].rolling(window=5).max()

# Rolling min
df["Rolling_Min"] = df["Price"].rolling(window=5).min()

# Rolling standard deviation
df["Rolling_Std"] = df["Price"].rolling(window=5).std()
