from sklearn.linear_model import LinearRegression
import streamlit as st
import sqlite3
import pandas as pd
import plotly.graph_objects as go
import datetime


# Function to get the article title
def get_title(date, index, topic, new):
    parts = date.split("-")
    path = f"data/{new}/articles/{topic}/{parts[0]
                                          }/month{parts[1]}/day{parts[2]}/{index}.txt"
    with open(path, "r", encoding="utf-8") as file:
        return file.read().splitlines()[0]


st.set_page_config(layout="wide")
st.title('Wordcount')

st.divider()

amount_of_plots = st.slider("Amount of Plots", 1, 5)

st.divider()
news_options = ["NYT", "Guardian", "Both"]
topics = ["Politics", "World", "Opinion", "Neutral", "All"]

for i in range(amount_of_plots):
    st.write(f"Plot {i+1}")
    selected_news = st.selectbox("Select News Source", news_options, key=i)
    selected_topic = st.selectbox("Select Topic", topics, key=i+amount_of_plots)

    # Connect to the database
    if selected_news == "Both":
        for i in ["NYT", "Guardian"]:
            conn = sqlite3.connect(f'Database/Wordcount/{i}.db')
            cursor = conn.cursor()
            if selected_topic == "All":
                rows = cursor.execute('SELECT date, wordcount FROM Politics UNION SELECT date, wordcount FROM World UNION SELECT date, wordcount FROM Opinion').fetchall()
            elif selected_topic == "Neutral":
                rows = cursor.execute('SELECT date, wordcount FROM Politics UNION SELECT date, wordcount FROM World').fetchall()
            else:
                rows = cursor.execute(f'SELECT date, wordcount FROM {selected_topic}').fetchall()

    else:
        conn = sqlite3.connect(f'Database/Wordcount/{selected_news}.db')
        cursor = conn.cursor()
        cursor.execute(f'SELECT date, wordcount FROM {selected_topic}')
        rows = cursor.fetchall()

    graph_data = pd.DataFrame(rows, columns=['date', 'wordcount'])
    graph_data['date'] = pd.to_datetime(graph_data['date'])

    st.divider()

# Year range selector
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

# Filter for a single year
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

st.markdown(
    f"<h4 style='text-align: center;'>Year: {year_range[0]} to {
        year_range[1]}, Month: {month_range[0]} to {month_range[1]}</h4>",
    unsafe_allow_html=True
)

st.divider()

# Filter data based on selected year and month range
filtered_graph_data = graph_data[
    (graph_data['date'].dt.year >= year_range[0]) &
    (graph_data['date'].dt.year <= year_range[1]) &
    (graph_data['date'].dt.month >= month_range[0]) &
    (graph_data['date'].dt.month <= month_range[1])
]

# Format the date column to exclude time
filtered_graph_data['date'] = filtered_graph_data['date'].dt.date


# Scatter plot
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
    name='Article',
    marker=dict(color='white', size=5)
))

# Linear Regression
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

# Update layout
fig.update_layout(
    title='Word Count Development',
    xaxis_title='Date',
    yaxis_title='Word Count',
    dragmode="pan" 
)

st.plotly_chart(fig, use_container_width=True)
st.divider()