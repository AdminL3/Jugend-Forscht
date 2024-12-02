# Streamlit and SQLite Tutorial

This tutorial will guide you through creating a Streamlit application that connects to an SQLite database, fetches data, and visualizes it using Plotly.

## Prerequisites

Ensure you have the following libraries installed:
- `streamlit`
- `sqlite3`
- `pandas`
- `plotly`

You can install them using pip:
```bash
pip install streamlit pandas plotly
```

## Step-by-Step Guide

### 1. Import Libraries

Start by importing the necessary libraries:
```python
import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
```

### 2. Configure Streamlit Page

Set the page layout to wide:
```python
st.set_page_config(layout="wide")
```

### 3. Define Helper Function

Create a function to get the article title:
```python
def get_title(date, index, topic, news):
    parts = date.split("-")
    path = f"data/{news}/articles/{topic}/{parts[0]}/month{parts[1]}/day{parts[2]}/{index}.txt"
    with open(path, "r", encoding="utf-8") as file:
        return file.read().splitlines()[0]
```

### 4. Streamlit Title and Selectors

Add a title and selectors for news source and topic:
```python
st.title('Wordcount')

news_options = ["NYT", "Guardian"]
topics = ["Politics", "World", "Opinion"]

selected_news = st.selectbox("Select News Source", news_options)
selected_topic = st.selectbox("Select Topic", topics)
```

### 5. Connect to Database

Connect to the SQLite database and fetch data:
```python
conn = sqlite3.connect(f'Database/Wordcount/{selected_news}.db')
cursor = conn.cursor()

cursor.execute(f'SELECT date, wordcount FROM {selected_topic}')
rows = cursor.fetchall()

data = pd.DataFrame(rows, columns=['date', 'wordcount'])
data['date'] = pd.to_datetime(data['date'])
```

### 6. Year Range Selector

Add a year range selector:
```python
st.subheader("Filter by Year Range")
min_year = data['date'].dt.year.min()
max_year = data['date'].dt.year.max()

year_range = st.slider(
    "Select Year Range",
    min_value=int(min_year),
    max_value=int(max_year),
    value=(int(min_year), int(max_year)),
    step=1
)
```

### 7. Month Range Selector

Add a month range selector if the year range is less than one year:
```python
if year_range[1] - year_range[0] < 1:
    st.divider()
    st.text("Your selected range is smaller than 1 year. You can specify a month range instead:")
    month_range = st.slider(
        "Select Month Range",
        min_value=1,
        max_value=12,
        value=(1, 12),
        step=1
    )
else:
    month_range = (1, 12)
```

### 8. Filter Data

Filter the data based on the selected year and month range:
```python
filtered_data = data[
    (data['date'].dt.year >= year_range[0]) &
    (data['date'].dt.year <= year_range[1]) &
    (data['date'].dt.month >= month_range[0]) &
    (data['date'].dt.month <= month_range[1])
]
filtered_data['date'] = filtered_data['date'].dt.date
```

### 9. Scatter Plot

Create and display a scatter plot:
```python
st.subheader("Scatter Plot:")
fig = px.scatter(
    filtered_data,
    x='date',
    y='wordcount',
    labels={'date': 'Date', 'wordcount': 'Word Count'},
    template='plotly_white'
)
fig.update_traces(marker=dict(size=5, opacity=0.7, color='blue'))
fig.update_layout(dragmode="pan")

st.plotly_chart(fig, use_container_width=True)
```

### 10. Top 10 Articles

Fetch and display the top 10 articles:
```python
cursor.execute(f'SELECT * FROM {selected_topic} ORDER BY wordcount DESC')
rows = cursor.fetchall()
data = pd.DataFrame(rows, columns=["ID", "Date", "Day Index", "Wordcount"])
data['Date'] = pd.to_datetime(data['Date'])

filtered_top_data = data[
    (data['Date'].dt.year >= year_range[0]) &
    (data['Date'].dt.year <= year_range[1]) &
    (data['Date'].dt.month >= month_range[0]) &
    (data['Date'].dt.month <= month_range[1])
]
filtered_top_data['Date'] = filtered_top_data['Date'].dt.date

with st.spinner("Fetching Articles..."):
    filtered_top_data['Title'] = filtered_top_data.apply(
        lambda row: get_title(row['Date'].strftime("%Y-%m-%d"), row['Day Index'], selected_topic, selected_news),
        axis=1
    )

st.subheader(f"Top 10 {selected_topic} Articles for {selected_news}")
st.dataframe(
    filtered_top_data[['Date', 'Day Index', 'Wordcount', 'Title']].head(10).set_index('Wordcount'),
    use_container_width=True
)
```

That's it! You now have a Streamlit application that connects to an SQLite database, fetches data, and visualizes it using Plotly.