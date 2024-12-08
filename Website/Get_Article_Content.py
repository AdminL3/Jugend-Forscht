import streamlit as st
from textblob import TextBlob

st.title('Get Content from Data')

st.divider()
st.subheader("Enter the data from the article you want to get:")

st.write("Input your content ID or manually input it down below:")
input = st.text_input("Press Enter to submit: ", f"{news_source}_{
                      topic}_{year}_{month}_{day}_{index}")

parts = input.split("_")
if len(parts) != 6:
    parts = input.split(" ")

try:
    news_source = parts[0]
    topic = parts[1]
    year = int(parts[2])
    month = int(parts[3])
    day = int(parts[4])
    index = int(parts[5])
except:
    st.error("""
Invalid input! Please input in the format:  
News_Topic_Year_Month_Day_Index 

Example inputs: 
- NYT_politics_2021_1_1_1 
- NYT politics 2022 1 1 1 

Alternatively, input manually below.
""")

    news_source = "NYT"
    topic = "politics"
    year = 2021
    month = 1
    day = 1
    index = 1


# 1a


st.divider()
news_sources = ["NYT", "Guardian"]
news_lower = [x.lower() for x in news_sources]
topics = ["politics", "world", "opinion"]
topics_lower = [x.lower() for x in topics]
news = st.selectbox("Select News Source", news_sources,
                    news_lower.index(news_source.lower()))
topic = st.selectbox("Select Topic", topics, topics_lower.index(topic.lower()))
year = st.slider("Year", 2010, 2022, year)
month = st.slider("Month", 1, 12, month)
day = st.slider("Day", 1, 31, day)
index = st.number_input("Index", 1, 50, index)

st.divider()
try:
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
except:
    st.error("Error: File not found  \nPlease check the input again.")
