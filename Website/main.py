import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")


# Function to get the article title
def get_title(date, index, topic, new):
    parts = date.split("-")
    path = f"data/{new}/articles/{topic}/{parts[0]
                                          }/month{parts[1]}/day{parts[2]}/{index}.txt"
    with open(path, "r", encoding="utf-8") as file:
        return file.read().splitlines()[0]


st.title('Wordcount')

news_options = ["NYT", "Guardian"]
topics = ["Politics", "World", "Opinion"]

selected_news = st.selectbox("Select News Source", news_options)
selected_topic = st.selectbox("Select Topic", topics)

# Connect to the database
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
filtered_data = data[
    (data['date'].dt.year >= year_range[0]) &
    (data['date'].dt.year <= year_range[1]) &
    (data['date'].dt.month >= month_range[0]) &
    (data['date'].dt.month <= month_range[1])
]

# Format the date column to exclude time
filtered_data['date'] = filtered_data['date'].dt.date

# Scatter plot
st.subheader("Scatter Plot:")
st.write(f"{selected_news} - {selected_topic} - {year_range[0]} - {month_range[0]} to {
         month_range[1]}" if one_year else f"{selected_news} - {selected_topic} - {year_range[0]} to {year_range[1]}")
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

# Get top 10 articles with applied filters
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

# Format the Date column to exclude time
filtered_top_data['Date'] = filtered_top_data['Date'].dt.date

# Add a Title column using the get_title function

with st.spinner("Fetching Articles..."):
    filtered_top_data['Title'] = filtered_top_data.apply(
        lambda row: get_title(row['Date'].strftime(
            "%Y-%m-%d"), row['Day Index'], selected_topic, selected_news),
        axis=1
    )

# Display top 10 filtered articles
st.subheader(f"Top 10 {selected_topic} Articles for {selected_news}")
st.dataframe(
    filtered_top_data[['Date', 'Day Index', 'Wordcount', 'Title']].head(
        10).set_index('Wordcount'),
    use_container_width=True
)