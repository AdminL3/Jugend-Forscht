from calendar import c, month
import os
import sqlite3

topics = ["politics", "world", "opinion"]

news = ["NYT", "Guardian"]
for n in news:
    print(f"- {n}")
    path = f"Database/Articlecount/Months/{n}.db"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    for t in topics:
        # Create tables
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {t} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            count INTEGER
        )""")

    conn.commit()

    for i, topic in enumerate(topics):
        print(f"  - {topic}")
        root_dir = f"data/{n}/articles/{topic}"

        count = 0
        years = [f for f in os.listdir(
            root_dir) if os.path.isdir(os.path.join(root_dir, f))]
        for year in years:
            print(f"    - {year}")
            year_dir = os.path.join(root_dir, year)
            months = [f for f in os.listdir(
                year_dir) if os.path.isdir(os.path.join(year_dir, f))]
            for month in months:
                # !Different from Days.py because count is not reset
                count = 0
                month_dir = os.path.join(year_dir, month)
                days = [f for f in os.listdir(
                    month_dir) if os.path.isdir(os.path.join(month_dir, f))]
                for day in days:
                    day_dir = os.path.join(month_dir, day)
                    # !Different from Days.py because +=
                    count += len(os.listdir(day_dir))

                month_n = int(month.split("month")[1])
                date = f"{year}-{month_n}"
                cursor.execute(f"""
                    INSERT INTO {topic} (date, count)
                    VALUES (?, ?)
                    """, (date, count))
                # print(f"Inserted {count} articles for {year}-{month}")
                if count == 0:
                    print(f"Error: {year}-{month}")
                    input()
                conn.commit()
