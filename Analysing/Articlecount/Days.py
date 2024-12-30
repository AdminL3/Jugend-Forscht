from calendar import c, month
import os
import sqlite3

topics = ["politics", "world", "opinion"]

news = ["NYT", "Guardian"]
for n in news:
    print(f"- {n}")
    conn = sqlite3.connect(f"Database/Articlecount/Days/{n}.db")
    cursor = conn.cursor()

    for t in topics:
        # Create tables
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {t} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year INTEGER,
            month INTEGER,
            day INTEGER,
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
                month_dir = os.path.join(year_dir, month)
                days = [f for f in os.listdir(
                    month_dir) if os.path.isdir(os.path.join(month_dir, f))]
                for day in days:
                    day_dir = os.path.join(month_dir, day)
                    count = len(os.listdir(day_dir))

                    month_n = int(month.split("month")[1])
                    day_n = int(day.split("day")[1])
                    cursor.execute(f"""
                    INSERT INTO {topic} (year, month, day, count)
                    VALUES ({year}, {month_n}, {day_n}, {count})
                    """)
                    # print(f"Inserted {count} articles for {year}-{month}-{day}")
                    if count == 0:
                        print(f"Error: {year}-{month}-{day}")
                        input()
                    conn.commit()
