# Persian to English Translator

A Python script that translates Persian words to English using the Google Translate API.

## Description

This tool reads Persian words from a CSV file and translates them to English using `googletrans` library, which interfaces with Google Translate. It's useful for language learning, data processing, or creating bilingual datasets.

## Features

- Reads Persian words from CSV file
- Translates Persian to English using Google Translate
- Handles unique values (removes duplicates)
- Asynchronous processing for better performance
- Supports multiple columns in CSV
- Prints translated results

## Requirements

- Python 3.7+
- pandas
- googletrans==4.0.0-rc1 (or higher)
- asyncio (standard library)
