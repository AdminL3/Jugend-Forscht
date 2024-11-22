import os
import sqlite3
from datetime import date


def get_idx(path):
    path_parts = path.split('/')
    idx = path_parts[-1][:-4]
    return idx


def get_date(path):
    path_parts = path.split('/')
    year = path_parts[3]
    month = path_parts[4][5:]
    day = path_parts[5][3:]
    return f"{year}-{month}-{day}"


def word_count(text):
    text = text.lower()
    text = text.replace("\n", " ")
    text = text.replace("  ", " ")
    text = text.replace(".", "")
    text = text.replace(",", "")
    words = text.split()
    word_count = len(words)
    return str(word_count)


conn = sqlite3.connect("Analysing\Wordcount\wordcount.db")
cursor = conn.cursor()
start_year = 2020
amount_years = 2
topics = ["politics", "world", "opinion"]

data = []
for topic in topics:
    print(topic)
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {topic} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            idx INTEGER NOT NULL,
            wordcount INTEGER NOT NULL
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
            files_path = f"data/NYT/articles/{topic}/{year}/month{month}/"
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
                index = get_idx(path)
                word_counter = word_count(article_text)

                data.append((date, word_counter, index))
# Step 3: Insert sample data into the table
    # print(data)
    cursor.executemany(
        f"INSERT INTO {topic} (date, wordcount, idx) VALUES (?, ?, ?)", data)
    conn.commit()
    data = []


# Step 4: Close the connection
conn.close()
