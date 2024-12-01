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

st.subheader(f"Scatter Plot for {selected_news} - {selected_topic}")
fig = px.scatter(
    data,
    x='date',
    y='wordcount',
    labels={'date': 'Date', 'wordcount': 'Word Count'},
    template='plotly_white'
)
fig.update_traces(marker=dict(size=5, opacity=0.7, color='blue'))

fig.update_layout(dragmode="pan")

st.plotly_chart(fig, use_container_width=True)
