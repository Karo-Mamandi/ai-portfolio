# Rolling Average
# Idea: Compute rolling averages for stock prices. Useful for financial trend analysis and time-series smoothing.

import pandas as pd

# Create a DataFrame with stock price data
stock = pd.DataFrame({"Price": [10, 12, 15, 20, 18, 22, 28, 9, 17, 23, 11, 19, 18, 15, 17]})

# Calculate rolling average with window size of 3
# First two rows will have NaN values (not enough data)
stock["Rolling"] = stock["Price"].rolling(window=3).mean()

# Display the stock prices with rolling averages
print("Rolling Average:\n", stock)
