# Streamlit and SQLite Tutorial

This tutorial will guide you through creating a Streamlit application that connects to an SQLite database, fetches data, and visualizes it using Plotly.

## Prerequisites

Ensure you have the following libraries installed:
- `streamlit`
- `sqlite3`
- `pandas`
- `plotly`

## Step-by-Step Guide

### 1. Import Libraries

Start by importing the necessary libraries:
```python
from sklearn.linear_model import LinearRegression
import streamlit as st
import sqlite3
import pandas as pd
import plotly.graph_objects as go
import datetime
```

---

### 2. Configure Streamlit Page

Set the page layout to wide:
```python
st.set_page_config(layout="wide")
st.title('Wordcount')
```

---

### 3. Define Helper Function

Create a function to get the article title:
```python
def get_title(date, index, topic, news):
    parts = date.split("-")
    path = f"data/{news}/articles/{topic}/{parts[0]}/month{parts[1]}/day{parts[2]}/{index}.txt"
    with open(path, "r", encoding="utf-8") as file:
        return file.read().splitlines()[0]
```

---

### 4. Streamlit Title and Selectors

Select the news source and topic:
```python
news_options = ["NYT", "Guardian"]
topics = ["Politics", "World", "Opinion"]

selected_news = st.selectbox("Select News Source", news_options)
selected_topic = st.selectbox("Select Topic", topics)
```

---

### 5. Connect to Database

Connect to the SQLite database and fetch data for the selected news and topic:
```python
conn = sqlite3.connect(f'Database/Wordcount/{selected_news}.db')
cursor = conn.cursor()

cursor.execute(f'SELECT date, wordcount FROM {selected_topic}')
rows = cursor.fetchall()

graph_data = pd.DataFrame(rows, columns=['date', 'wordcount'])
graph_data['date'] = pd.to_datetime(graph_data['date']
```

---

### 6. Year Range Selector

Add a year range selector:
```python
st.subheader("Filter by Year Range")
min_year = graph_data['date'].dt.year.min()
max_year = graph_data['date'].dt.year.max()

year_range = st.slider(
    "Select Year Range",
    min_value=int(min_year),
    max_value=int(max_year),
    value=(int(min_year), int(max_year)),
    step=1
)
```

---

### 7. Month Range Selector

Add a month range selector if the year range is less than one year:
```python
if year_range[1] - year_range[0] < 1:
    one_year = True
else:
    one_year = False

if one_year:
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

---

### 8. Filter Data

Filter the data based on the selected year and month range:
```python
filtered_graph_data = graph_data[
    (graph_data['date'].dt.year >= year_range[0]) &
    (graph_data['date'].dt.year <= year_range[1]) &
    (graph_data['date'].dt.month >= month_range[0]) &
    (graph_data['date'].dt.month <= month_range[1])
]
filtered_graph_data['date'] = filtered_graph_data['date'].dt.date
```

---

### 9. Scatter Plot

Create and display a scatter plot:
```python
# title
st.subheader("Scatter Plot:")
st.write(f"{selected_news} - {selected_topic} - {year_range[0]} - {month_range[0]} to {
         month_range[1]}" if one_year else f"{selected_news} - {selected_topic} - {year_range[0]} to {year_range[1]}")

# Create scatter plot
fig = go.Figure()

# Add scatter points
fig.add_trace(go.Scatter(
    x=filtered_graph_data['date'],
    y=filtered_graph_data['wordcount'],
    mode='markers',
    name='Data Points',
    marker=dict(color='white', size=5)
))
```

---

### 10. Regression Line

Add a regression line to the scatter plot:
```python
model = LinearRegression()
X = pd.to_numeric(filtered_graph_data['date'].map(datetime.datetime.toordinal)).values.reshape(-1, 1)
y = filtered_graph_data['wordcount'].values

model.fit(X, y)
y_pred = model.predict(X)

# Add regression line
fig.add_trace(go.Scatter(
    x=filtered_graph_data['date'],
    y=y_pred,
    mode='lines',
    name='Regression Line',
    line=dict(color='red', width=2)
))
```

---

## 11. Display Plot

Display the plot:
```python
fig.update_layout(
    title='Word Count Development',
    xaxis_title='Date',
    yaxis_title='Word Count',
    dragmode="pan"
)

st.plotly_chart(fig, use_container_width=True)
st.divider()
```

---

### 12. Top 10 Articles

Fetch and display the top 10 articles in a table:
```python
cursor.execute(f'SELECT * FROM {selected_topic} ORDER BY wordcount DESC')
rows = cursor.fetchall()
# create a dataframe
top_data = pd.DataFrame(rows, columns=["ID", "Date", "Day Index", "Wordcount"])
# convert the Date column to datetime
top_data['Date'] = pd.to_datetime(top_data['Date'])

filtered_top_data = top_data[
    (top_data['Date'].dt.year >= year_range[0]) &
    (top_data['Date'].dt.year <= year_range[1]) &
    (top_data['Date'].dt.month >= month_range[0]) &
    (top_data['Date'].dt.month <= month_range[1])
]

# Format the Date column to exclude time
filtered_top_data['Date'] = filtered_top_data['Date'].dt.date

# Add a Title column using the get_title function

with st.spinner("Fetching Articles..."):
    filtered_top_data['Title'] = filtered_top_data.apply(
        lambda row: get_title(row['Date'].strftime(
            "%Y-%m-%d"), row['Day Index'], selected_topic, selected_news),
        axis=1
    )

st.subheader(f"Top 10 {selected_topic} Articles for {selected_news}")


filtered_top_data = filtered_top_data.head(10)
styled_dataframe = filtered_top_data.style.applymap(
    lambda x: 'color: yellow', subset=['Wordcount'])

st.dataframe(
    styled_dataframe,
    use_container_width=True,
    hide_index=True,
    column_config={
        "ID": st.column_config.Column(width=-100),
        "Wordcount": st.column_config.Column(width=-100),
        "Date": st.column_config.Column(width=-100),
        "Day Index": st.column_config.Column(width=-100),
        "Title": st.column_config.Column(width=600)
    }
)
```
---

> [!NOTE]  
> That's it! You now have a Streamlit application that connects to an SQLite database, fetches data, and visualizes it using Plotly.