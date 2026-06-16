# Import required libraries 
import pandas as pd
import asyncio  # For asynchronous operations
from googletrans import Translator  # For Google Translate API

# Read Persian words from CSV file
data = pd.read_csv("persian_word.csv")

# Create translator instance
translator = Translator()

# Initialize dictionary to store translations
translations = {}

# Async function to translate words
async def main():
    # Loop through each column in the CSV
    for column in data.columns:
        # Get unique values from column (remove duplicates and NaN)
        unique_values = data[column].dropna().unique()

        # Translate each unique value
        for element in unique_values:
            # Asynchronously translate Persian to English
            result = await translator.translate(str(element))
            # Store translation in dictionary
            translations[element] = result.text


# Run the async main function
asyncio.run(main())

# Print all translations
for item in translations.items():
    print(item)
