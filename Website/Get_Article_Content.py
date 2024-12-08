import streamlit as st
from textblob import TextBlob

st.title('Get Content from Data')

st.divider()
st.subheader("Enter the data from the article you want to get:")

# make some space
st.write("")

news = st.selectbox("Select News Source", ["NYT", "Guardian"])
topic = st.selectbox("Select Topic", ["politics", "world", "opinion"])
year = st.slider("Year", 2010, 2022)
month = st.slider("Month", 1, 12)
day = st.slider("Day", 1, 31)
index = st.number_input("Index", 1, 50, 1)

run = st.button("Get Content")

with st.spinner("Getting Article Content..."):
    if run:
        st.subheader("Article Content: ")
        st.write(f"{news} - {topic} - {year}/{month}/{day} - {index}")
        st.divider()
        file_path = f"data/{news}/articles/{topic}/{
            year}/month{month:02}/day{day:02}/{index}.txt"
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        st.text(content)

        st.divider()

        st.subheader("More Information on the text:")
        st.write("")
        st.write("1. Number of Words: ", len(content.split()))
        st.write("2. Number of Characters: ", len(content))
        st.write("3. Number of Sentences: ", content.count("."))
        blob = TextBlob(content)
        sentiment_polarity = blob.sentiment.polarity
        sentiment_subjectivity = blob.sentiment.subjectivity

        st.write("4. Polarity: ", round(sentiment_polarity*100, 2), "%")
        st.write("5. Subjectivity: ", round(
            sentiment_subjectivity*100, 2), "%")
