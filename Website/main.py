import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Streamlit App
st.title('Wordcount')

# Dropdown menu to select the news source
news_options = ["NYT", "Guardian"]
topics = ["Politics", "World", "Opinion"]

# Selection dropdowns
selected_news = st.selectbox("Select News Source", news_options)
selected_topic = st.selectbox("Select Topic", topics)

# Connect to the database for the selected news source
conn = sqlite3.connect(f'Database/Wordcount/{selected_news}.db')
cursor = conn.cursor()

# Fetch data
cursor.execute(f'SELECT date, wordcount FROM {selected_topic}')
rows = cursor.fetchall()

# Convert to Pandas DataFrame with correct column names
data = pd.DataFrame(rows, columns=['date', 'wordcount'])

# Convert the 'date' column to datetime
data['date'] = pd.to_datetime(data['date'])

# Interactive Scatter Plot
st.subheader(f"Scatter Plot for {selected_news} - {selected_topic}")
fig = px.scatter(
    data,
    x='date',
    y='wordcount',
    title=f"Scatter Plot for {selected_news} - {selected_topic}",
    labels={'date': 'Date', 'wordcount': 'Word Count'},
    template='plotly_white'
)
fig.update_traces(marker=dict(size=5, opacity=0.7, color='blue'))

fig.update_layout(dragmode="pan")

st.plotly_chart(fig, use_container_width=True)
