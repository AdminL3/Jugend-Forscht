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
                for day in os.listdir(files_path):
                    day_path = os.path.join(files_path, day)
                    if os.path.isdir(day_path):
                        files = [file for file in os.listdir(
                            day_path) if file.endswith('.txt')]
                        daily_count = len(files)
                        monthly_total += daily_count

                        # Insert daily count into the articles table
                        cursor.execute("""
                            INSERT INTO articles (topic_id, year, month, day, count)
                            VALUES (?, ?, ?, ?, ?)
                        """, (topic_id, year, month, day, daily_count))

            # Add to yearly and topic totals
            yearly_total += monthly_total
            topic_total += monthly_total

            # Insert monthly total into the monthly_totals table
            cursor.execute("""
                INSERT INTO monthly_totals (topic_id, year, month, total_count)
                VALUES (?, ?, ?, ?)
            """, (topic_id, year, month, monthly_total))

        # Insert yearly total into the yearly_totals table
        cursor.execute("""
            INSERT INTO yearly_totals (topic_id, year, total_count)
            VALUES (?, ?, ?)
        """, (topic_id, year, yearly_total))

    # Insert topic-wide total into the topic_totals table
    cursor.execute("""
        INSERT INTO topic_totals (topic_id, total_count)
        VALUES (?, ?)
    """, (topic_id, topic_total))

    conn.commit()

conn.close()
