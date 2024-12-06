# News Article Word Count Analysis App

## Overview

A Streamlit-powered web application for analyzing word count trends across different news sources and topics. This interactive tool allows users to:

- Visualize word count trends for multiple news sources
- Apply custom filters for years and months
- Generate scatter plots with regression analysis
- Explore top articles based on word count

## Features

- **Multi-Source Analysis**: Compare word count trends across NYT and Guardian
- **Topic-Based Filtering**: Analyze data from Politics, World, and Opinion sections
- **Interactive Visualization**:
  - Customizable plot colors
  - Dynamic year and month range selection
  - Linear regression trend lines
- **Top Articles Exploration**:
  - View top 10 articles by word count
  - Filtered by news source and topic

## Prerequisites

### Required Libraries

- streamlit
- sqlite3
- pandas
- plotly
- scikit-learn

### Database Structure

Create a `Database` folder with the following structure:

```
Database/
│
├── wordcount/
│   ├── NYT.db
│   └── Guardian.db
│
└── Titles/
    ├── NYT.db
    └── Guardian.db
```

#### Database Tables

Each database should include tables:

- `Politics`
- `World`
- `Opinion`

Required columns:

- `date`
- `wordcount`
- `day_index`
- `title`

## Installation

1. Clone the repository
2. Install required libraries:
   ```bash
   pip install streamlit pandas plotly scikit-learn
   ```
3. Ensure your SQLite databases are properly configured
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage Guide

1. Select number of plots (1-7)
2. For each plot:
   - Choose news source
   - Select topic
   - Pick visualization colors
3. Use year and month range selectors to filter data
4. View scatter plot with word count trends
5. Explore top articles in the table below

## Customization

- Adjust color schemes
- Modify plot styles
- Add additional data sources

## Limitations

- Requires pre-populated SQLite databases
- Performance may degrade with large datasets
- Limited to word count analysis

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

[Specify your license here]

## Contact

[Your contact information or project maintainer details]
