import os
import sqlite3
from datetime import date
from textblob import TextBlob


conn = sqlite3.connect("Analysing\Sentimental\sentiment.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS World (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        polarity INTEGER NOT NULL,
        subjectivity INTEGER NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Politics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        polarity INTEGER NOT NULL,
        subjectivity INTEGER NOT NULL
    )
''')
conn.commit()


data = []


def get_date(path):
    path_parts = path.split('/')
    year = path_parts[3]
    month = path_parts[4][5:]
    day = path_parts[5][3:]
    return f"{year}-{month}-{day}"


def get_sentiment(text):
    blob = TextBlob(text)

    # Sentiment analysis
    sentiment_polarity = blob.sentiment.polarity
    sentiment_subjectivity = blob.sentiment.subjectivity
    return [sentiment_polarity, sentiment_subjectivity]


start_year = 2020
amount_years = 2
topics = ["politics", "world"]

for topic in topics:
    print(topic)
    for i in range(amount_years):
        year = start_year + i
        print(year)
        for j in range(12):
            numbers = [str(h).zfill(2) for h in range(1, 13)]
            month = numbers[j]
            print(month)
            files_path = f"data/articles/{topic}/{year}/month{month}/"
            days = []
            if os.path.exists(files_path):
                for item in os.listdir(files_path):
                    item_path = os.path.join(files_path, item)
                    days.append(item_path)
            else:
                print(f"Folder does not exist: {files_path}")

            files = []
            for day in days:
                for file in os.listdir(day):
                    if file.endswith('.txt'):
                        files.append(os.path.join(day, file))

            for file in files:
                with open(file, 'r', encoding='utf-8') as f:
                    article_text = f.read()
                path = file.replace("\\", "/")

                # print(path)
                date = get_date(path)

                sentiment = get_sentiment(article_text)

                data.append((date, sentiment[0], sentiment[1]))
# Step 3: Insert sample data into the table
    # print(data)
    cursor.executemany(
        f"INSERT INTO {topic} (date, polarity, subjectivity) VALUES (?, ?, ?)", data)
    conn.commit()
    data = []


# Step 4: Close the connection
conn.close()
