# Visualizing the Data in a Website 🌐

> [!Important]
> View an explanation of the code [here](./Streamlit.md).

## Overview

This Streamlit application provides an interactive tool for analyzing word count across different news sources (New York Times and The Guardian) and various topics. Users can visualize word count trends, apply filters, and explore top articles.

## Features

### Data Visualization

- Interactive scatter plot showing word count development
- Linear regression lines for trend analysis
- Customizable color selection for each dataset
- Multiple dataset comparison (up to 7 plots)

### Filtering Options

- Select news sources: NYT, Guardian, or Both
- Filter by topics: Politics, World, Opinion, Neutral, or All
- Year range selection
- Month range selection for more granular analysis

### Top Articles

- Displays top 10 articles based on word count
- Supports filtering by news source, topic, year, and month

## Prerequisites

### Required Libraries

- streamlit
- sklearn
- sqlite3
- pandas
- plotly

### Database Structure

The application expects SQLite databases with the following structure:

- Located in `Database/wordcount/` directory
- Separate databases for NYT and Guardian
- Tables: Politics, World, Opinion
- Columns should include: date, wordcount

## Usage Tips

- Recommended to view 2 plots at a time for better visualization
- Use color pickers to customize plot appearance
- Adjust year and month ranges to focus on specific time periods

## Limitations

- Title retrieval only works when a specific news source and topic are selected
- Maximum of 7 plots can be compared simultaneously
