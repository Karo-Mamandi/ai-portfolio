# GroupBy Example
# Idea: Group sales data by day and calculate totals. A practical example of aggregation in business analytics.

import pandas as pd

# Create a DataFrame with sales data
sales = pd.DataFrame({
    "Day": ["Mon", "Mon", "Tue", "Tue", "Tue", "Tue", "Mon", "Mon", "Tue"],  # Day of the week
    "Amount": [100, 200, 150, 300, 120, 220, 180, 190, 140]            # Sales amounts
})

# Group by Day and calculate total sales for each day
print("Total Sales per Day:\n", sales.groupby("Day")["Amount"].sum())
