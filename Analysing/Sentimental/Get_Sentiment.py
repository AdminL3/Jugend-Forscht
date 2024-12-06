import os
import sqlite3
from datetime import date
from textblob import TextBlob


def get_idx(path):
    path_parts = path.split('/')
    idx = path_parts[-1][:-4]
    return idx


def get_date(path):
    path_parts = path.split('/')
    year = path_parts[4]
    month = path_parts[5][5:]
    day = path_parts[6][3:]
    return f"{year}-{month}-{day}"


def get_sentiment(text):
    blob = TextBlob(text)

    # Sentiment analysis
    sentiment_polarity = blob.sentiment.polarity
    sentiment_subjectivity = blob.sentiment.subjectivity
    return [sentiment_polarity, sentiment_subjectivity]


start_year = 2010
amount_years = 1
topics = ["politics", "world", "opinion"]
news = ["NYT", "Guardian"]
for new in news:
    database_path = f"Database/Sentiment/{new}.db"
    os.makedirs(os.path.dirname(database_path), exist_ok=True)
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    data = []
    for topic in topics:
        print(topic)
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {topic} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                idx INTEGER NOT NULL,
                polarity INTEGER NOT NULL,
                subjectivity INTEGER NOT NULL
                )
        ''')
        conn.commit()
        for i in range(amount_years):
            year = start_year + i
            print(year)
            for j in range(12):
                numbers = [str(h).zfill(2) for h in range(1, 13)]
                month = numbers[j]
                print(month)
                files_path = f"data/{new}/articles/{topic}/{year}/month{month}/"
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

                    date = get_date(path)

                    sentiment = get_sentiment(article_text)

                    data.append(
                        (date, get_idx(path), sentiment[0], sentiment[1]))

        cursor.executemany(
            f"INSERT INTO {topic} (date, idx, polarity, subjectivity) VALUES (?, ?, ?, ?)", data)
        conn.commit()
        data = []

    # Step 4: Close the connection
    conn.close()
