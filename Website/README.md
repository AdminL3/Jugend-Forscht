# Visualizing the Data in a Website 🌐

> [!IMPORTANT]
> Find out how the Code works [here](./Streamlit.md)

## Features

- [x] **Multi-Source Analysis**:
  - Compare word count trends across NYT and Guardian
- [x] **Topic-Based Filtering**:
  - Analyze data from Politics, World, and Opinion sections
- [x] **Interactive Visualization**:

  - Customizable plot colors
  - Dynamic year and month range selection
  - Linear regression trend lines

- [x] **Top Articles Exploration**:

  - View top 10 articles by word count
  - Filtered by news source and topic

- [x] **More**

---

## Prerequisites

### Required Libraries

- streamlit
- sqlite3
- pandas
- plotly
- scikit-learn

---

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

---

## Usage Guide

1. Select number of plots (1-7)
2. For each plot:
   - Choose news source
   - Select topic
   - Pick visualization colors
3. Use year and month range selectors to filter data
4. View scatter plot with word count trends
5. Explore top articles in the table below

---

## Customization

- Adjust color schemes
- Modify plot styles
- Add additional data sources

---

## Limitations

- Requires pre-populated SQLite databases
- Performance may degrade with large datasets
- Limited to word count analysis
