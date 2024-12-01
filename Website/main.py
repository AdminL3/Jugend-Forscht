from calendar import month
import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title('Wordcount')

news_options = ["NYT", "Guardian"]
topics = ["Politics", "World", "Opinion"]

selected_news = st.selectbox("Select News Source", news_options)
selected_topic = st.selectbox("Select Topic", topics)

conn = sqlite3.connect(f'Database/Wordcount/{selected_news}.db')
cursor = conn.cursor()

cursor.execute(f'SELECT date, wordcount FROM {selected_topic}')
rows = cursor.fetchall()

data = pd.DataFrame(rows, columns=['date', 'wordcount'])
data['date'] = pd.to_datetime(data['date'])

# Year range selector
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
if year_range[1]-year_range[0] < 2:
    st.text("Your selected range is smaller than 2 years.")
    month_range = st.slider(
        "You can specify a month range instead",
        min_value=1,
        max_value=12,
        value=(1, 12),
        step=1
    )
else:
    month_range = (1, 12)

# Filter data based on selected year range
filtered_data = data[(data['date'].dt.year >= year_range[0])
                     & (data['date'].dt.year <= year_range[1])]

st.subheader(f"Scatter Plot for {selected_news} - {selected_topic}")
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

st.divider()

# Get top 10 articles
cursor.execute(f'SELECT * FROM {selected_topic} ORDER BY wordcount DESC')
rows = cursor.fetchall()
data = pd.DataFrame(rows, columns=["ID", "Date", "Index", "Wordcount"])
data['Date'] = pd.to_datetime(data['Date'])

# Filter for the same year range
filtered_top_data = data[
    (data['Date'].dt.year >= year_range[0]) & (
        data['Date'].dt.year <= year_range[1])
]

st.subheader(f"Top 10 {selected_topic} Articles for the {selected_news}")
st.dataframe(filtered_top_data.head(10), use_container_width=True)
