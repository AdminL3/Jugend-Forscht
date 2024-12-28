import os
import sqlite3

from altair import Y

topics = ["politics", "world", "opinion"]
years = [2010, 2011, 2020, 2021]
news = ["NYT", "Guardian"]
for n in news:
    months_conn = sqlite3.connect(f"Database/Articlecount/Months/{n}.db")
    cursor_months = months_conn.cursor()

    for t in topics:
        # Create tables
        cursor_months.execute(f"""
        CREATE TABLE IF NOT EXISTS {t} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year INTEGER,
            month INTEGER,
            day INTEGER,
            count INTEGER
        )""")

    days_conn = sqlite3.connect(f"Database/Articlecount/Days/{n}.db")
    cursor_days = days_conn.cursor()

    for i, topic in enumerate(topics):
        print(f"Processing topic: {topic}")
        root_dir = f"data/{n}/articles/{topic}"

        count = 0
        for year in years:
            for month in range(1, 13):
                cursor_days.execute(f"""
                SELECT year, month, day, count FROM {topic}
                WHERE year = {year} AND month = {month}
                """)
                rows = cursor_days.fetchall()
                if len(rows) == 0:
                    count = 0
                else:
                    for row in rows:
                        count += row[3]
                    print(f"{year}-{month} has {count} articles")

                    cursor_months.execute(f"""
                    INSERT INTO {topic} (year, month, count)
                    VALUES ({year}, {month}, {count})
                    """)

                    count = 0
