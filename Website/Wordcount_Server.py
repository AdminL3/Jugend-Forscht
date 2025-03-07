from sklearn.linear_model import LinearRegression
import streamlit as st
import sqlite3
import pandas as pd
import plotly.graph_objects as go
import datetime
import requests

db_url = "https://raw.githubusercontent.com/AdminL3/Jugend-Forscht/main/Database/Wordcount"
dbs = ["Guardian.db", "NYT.db"]
for db in dbs:
    response = requests.get(f"{db_url}/{db}")
    with open(db, "wb") as file:
        file.write(response.content)

for db in dbs:
    response = requests.get(
        "https://raw.githubusercontent.com/AdminL3/Jugend-Forscht/main/Database/Titles/"+db)
    with open(f"T{db}", "wb") as file:
        file.write(response.content)


def get_data_from_db_with_filter(selected_news, selected_topic, name, selectors, order=""):
    if selected_news == "Both":
        for i in ["NYT", "Guardian"]:
            conn = sqlite3.connect(f'{i}.db')
            cursor = conn.cursor()
            if selected_topic == "All":
                rows = cursor.execute(
                    f'SELECT {selectors} FROM Politics UNION SELECT {selectors} FROM World UNION SELECT {selectors} FROM Opinion {order}').fetchall()
            elif selected_topic == "Neutral":
                rows = cursor.execute(
                    f'SELECT {selectors} FROM Politics UNION SELECT {selectors} FROM World {order}').fetchall()
            else:
                rows = cursor.execute(f'SELECT {selectors} FROM {
                                      selected_topic} {order}').fetchall()

    else:
        conn = sqlite3.connect(f'{selected_news}.db')
        cursor = conn.cursor()
        if selected_topic == "All":
            rows = cursor.execute(
                f'SELECT {selectors} FROM Politics UNION SELECT {selectors} FROM World UNION SELECT {selectors} FROM Opinion {order}').fetchall()
        elif selected_topic == "Neutral":
            rows = cursor.execute(
                f'SELECT {selectors} FROM Politics UNION SELECT {selectors} FROM World {order}').fetchall()
        else:
            rows = cursor.execute(f'SELECT {selectors} FROM {
                                  selected_topic} {order}').fetchall()
    return rows


st.set_page_config(layout="wide")
st.title('Wordcount')

st.divider()
st.subheader(
    "I recommended 2 Plots at a time")
st.write("- for better visualization,")
st.write("- performance,")
st.write("- and to avoid overlapping data points.")

# make some space
for i in range(4):
    st.write("")

amount_of_plots = st.slider("Amount of Plots", 1, 7)

st.divider()
colors = ['#1f77b4', '#ff7f0e', "#008000", "#fff", "#fff", "#fff", "#fff"]
colors_reg = ['#0000ff', '#ff0000', "#000000", "#000", "#000", "#000", "#000"]
news_options = ["NYT", "Guardian", "Both"]
topics = ["Politics", "World", "Opinion", "Neutral", "All"]

all_data = []
news_selectors = []
topic_selectors = []
for i in range(amount_of_plots):
    st.write(f"Dataset number {i+1}")
    selected_news = st.selectbox("Select News Source", news_options, key=i)
    selected_topic = st.selectbox(
        "Select Topic", topics, key=i+amount_of_plots)
    selected_color = st.color_picker(
        "Select Color", key=i+2*amount_of_plots, value=colors[i])
    selected_reg_color = st.color_picker(
        "Select Regression Color", key=i+3*amount_of_plots, value=colors_reg[i])

    news_selectors.append(selected_news)
    topic_selectors.append(selected_topic)

    # Get data from database based on selected news and topic
    rows = get_data_from_db_with_filter(
        selected_news, selected_topic, "wordcount", "date, wordcount")

    graph_data = pd.DataFrame(rows, columns=['date', 'wordcount'])
    graph_data['date'] = pd.to_datetime(graph_data['date'])
    all_data.append([graph_data, selected_news, selected_topic,
                    selected_color, selected_reg_color])
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
    st.text(f"Your selected range is smaller than 1 year. You can specify a month range for {
            year_range[0]}:")
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

# Scatter plot
# title
st.subheader("Scatter Plot:")
st.write(f"{year_range[0]} - {month_range[0]} to {
    month_range[1]}" if one_year else f"{year_range[0]} to {year_range[1]}")
if st.button("Generate Graph"):
    with st.spinner("Generating Graph..."):
        try:
            st.write(
                "Note: Click on elements in the Legend to make them invisible.")
            # Filter data based on selected year and month range
            for i in range(amount_of_plots):
                all_data[i][0] = all_data[i][0][
                    (all_data[i][0]['date'].dt.year >= year_range[0]) &
                    (all_data[i][0]['date'].dt.year <= year_range[1]) &
                    (all_data[i][0]['date'].dt.month >= month_range[0]) &
                    (all_data[i][0]['date'].dt.month <= month_range[1])
                ]

                # Format the date column to exclude time
                all_data[i][0]['date'] = all_data[i][0]['date'].dt.date

            # Create scatter plot
            fig = go.Figure()

            # Add scatter points
            for i in range(amount_of_plots):
                fig.add_trace(go.Scatter(
                    x=all_data[i][0]['date'],
                    y=all_data[i][0]['wordcount'],
                    mode='markers',
                    name='Article Count: ' +
                    all_data[i][1] + " - " + all_data[i][2],
                    marker=dict(color=all_data[i][3], size=5)
                ))

            for i in range(amount_of_plots):
                # Linear Regression
                model = LinearRegression()
                X = pd.to_numeric(all_data[i][0]['date'].map(
                    datetime.datetime.toordinal)).values.reshape(-1, 1)
                y = all_data[i][0]['wordcount'].values

                model.fit(X, y)
                y_pred = model.predict(X)

                # Add regression line
                fig.add_trace(go.Scatter(
                    x=all_data[i][0]['date'],
                    y=y_pred,
                    mode='lines',
                    name='Regression Line: ' +
                    all_data[i][1] + " - " + all_data[i][2],
                    line=dict(color=all_data[i][4], width=2)
                ))

            # Update layout
            fig.update_layout(
                title='Word Count Development',
                xaxis_title='Date',
                yaxis_title='Word Count',
                dragmode="pan"
            )

            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error("**Error:**  \nAn error occurred while generating the graph.  \nIt looks like the range you selected doesn't have any data.  \nCurrenly available data ranges are 2010 - 2010 and 2020 - 2022.")

st.divider()


# Get top 10 articles with applied filters
st.header(f"Top 10 Articles for {year_range[0]} - {month_range[0]} to {
    month_range[1]}" if one_year else f"Top 10 Articles for {year_range[0]} to {year_range[1]}")
for i in range(amount_of_plots):
    selected_news = news_selectors[i]
    selected_topic = topic_selectors[i]

    # Get data from database based on selected news and topic
    rows = get_data_from_db_with_filter(
        selected_news, selected_topic, "wordcount", "*", "ORDER BY wordcount DESC")

    # create a dataframe
    top_data = pd.DataFrame(
        rows, columns=["ID", "Date", "Day Index", "Wordcount"])
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

    st.write(f"Top Articles for {selected_news} - {selected_topic}")
    if st.button("Generate Table", key=i+4*amount_of_plots):
        filtered_top_data = filtered_top_data.head(10)
        if selected_news == "Both" or selected_topic == "All" or selected_topic == "Neutral":
            st. write(
                "Currently, we only support fetching titles for a single news source and a single topic.")
        else:
            with st.spinner("Fetching Articles..."):
                conn2 = sqlite3.connect(f'T{selected_news}.db')
                cursor2 = conn2.cursor()
                titles = []
                for _, row in filtered_top_data.iterrows():
                    date = row['Date'].strftime("%Y-%m-%d")
                    cursor2.execute(
                        f"SELECT title FROM {selected_topic.lower()} WHERE date=? AND idx=?", (date, row['Day Index']))
                    title = cursor2.fetchone()[0]
                    titles.append(title)
                filtered_top_data['Title'] = titles

        filtered_top_data['Content ID'] = filtered_top_data.apply(
            lambda row: f"{selected_news}_{selected_topic}_{
                row["Date"]}_{row['Day Index']}",
            axis=1
        )

        # Apply styles and show the dataframe
        styled_dataframe = filtered_top_data.style.applymap(
            lambda x: 'color: yellow', subset=['Wordcount']
        )

        st.dataframe(
            styled_dataframe,
            use_container_width=True,
            hide_index=True,
            column_config={
                "ID": st.column_config.Column(width=-100),
                "Wordcount": st.column_config.Column(width=-100),
                "Date": st.column_config.Column(width=-100),
                "Day Index": st.column_config.Column(width=-100),
                "Title": st.column_config.Column(width=600),
                "Content ID": st.column_config.Column(width=100)
            }
        )

st.write("Tip: Copy the last column to the Get Article Content page to get the content of the article.")
