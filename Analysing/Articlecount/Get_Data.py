import os
import sqlite3

data_root = "data/articles"
start_year = 2020
amount_years = 2
topics = ["politics", "world"]

conn = sqlite3.connect("Analysing/Articlecount/articlecount.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    count INTEGER,
    FOREIGN KEY (topic_id) REFERENCES topics (id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS monthly_totals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id INTEGER,
    year INTEGER,
    month INTEGER,
    total_count INTEGER,
    FOREIGN KEY (topic_id) REFERENCES topics (id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS yearly_totals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id INTEGER,
    year INTEGER,
    total_count INTEGER,
    FOREIGN KEY (topic_id) REFERENCES topics (id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS topic_totals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id INTEGER,
    total_count INTEGER,
    FOREIGN KEY (topic_id) REFERENCES topics (id)
)
""")
conn.commit()

data = []

topic_id = -1
for topic in topics:
    print(f"Processing topic: {topic}")
    topic_id += 1

    topic_total = 0  # Initialize topic-wide total for all years

    for i in range(amount_years):
        year = start_year + i
        print(f"  Year: {year}")
        yearly_total = 0  # Initialize yearly total

        for j in range(12):
            month = str(j + 1).zfill(2)
            print(f"Month: {month}")
            files_path = os.path.join(
                data_root, topic, str(year), f"month{month}")
            monthly_total = 0

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

                word_counter = word_count(article_text)

                data.append((date, word_counter))
# Step 3: Insert sample data into the table
    print(data)
    cursor.executemany(
        f"INSERT INTO {topic} (date, wordcount) VALUES (?, ?)", data)
    conn.commit()
    data = []


# Step 4: Close the connection
conn.close()
