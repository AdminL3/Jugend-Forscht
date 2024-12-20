import os
import sqlite3

data_root = "data/NYT/articles"
start_year = 2020
amount_years = 2
topics = ["politics", "world", "opinion"]

conn = sqlite3.connect("Database/Articlecount/articlecount.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id INTEGER,
    date TEXT,
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

topic_id = -1
for topic in topics:
    print(f"Processing topic: {topic}")
    topic_id += 1

    topic_total = 0  # Initialize topic-wide total for all years

    for i in range(amount_years):
        year = start_year + i
        print(f"Year: {year}")
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

                        # Construct the date in YYYY-MM-DD format# Correct handling of 'day'
                        # Extract only digits
                        day_numeric = ''.join(filter(str.isdigit, day))
                        date = f"{year}-{month}-{day_numeric.zfill(2)}"

                        # Insert daily count into the articles table
                        cursor.execute("""
                            INSERT INTO articles (topic_id, date, count)
                            VALUES (?, ?, ?)
                        """, (topic_id, date, daily_count))

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
