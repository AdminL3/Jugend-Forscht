import os
import sqlite3
from datetime import date

# Step 1: Connect to an SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect("Analysing\Wordcount\wordcount.db")
cursor = conn.cursor()

# Step 2: Create the table to store dates and numbers
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Wordcount (
        id INTEGER PRIMARY KEY AUTOINCREMENT,   -- unique identifier for each entry
        date TEXT NOT NULL,                     -- column to store the date in text format
        number INTEGER NOT NULL                 -- column to store the associated number
    )
''')
conn.commit()


# Get the data
sample = (str(date(2024, 11, 11)), 10)
data = []


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


start_year = 2020
amount_years = 1
topics = ["politics"]

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

                print(path)
                date = get_date(path)

                word_counter = word_count(article_text)

                data.append((date, word_counter))


# Step 3: Insert sample data into the table

cursor.executemany(
    "INSERT INTO Wordcount (date, number) VALUES (?, ?)", data)
conn.commit()

# Step 4: Close the connection
conn.close()