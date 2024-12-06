import os
import sqlite3


def get_title(date, index, topic, new):
    parts = date.split("-")
    path = f"data/{new}/articles/{topic}/{parts[0]
                                          }/month{parts[1]}/day{parts[2]}/{index}.txt"
    with open(path, "r", encoding="utf-8") as file:
        return file.read().splitlines()[0]


base_path = 'data'
topics = ['Politics', 'World', 'Opinion']
news = ['NYT', 'Guardian']
for n in news:
    database_path = f'Database/Titles/{n}.db'
    os.makedirs(os.path.dirname(database_path), exist_ok=True)
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    for topic in topics:
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {topic} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                idx INTEGER NOT NULL,
                title TEXT NOT NULL
            )
        ''')
        topic_path = os.path.join(base_path, n, 'articles', topic)
        for year in os.listdir(topic_path):
            year_path = os.path.join(topic_path, year)
            for month in os.listdir(year_path):
                month_path = os.path.join(year_path, month)
                for day in os.listdir(month_path):
                    day_path = os.path.join(month_path, day)
                    for file_name in os.listdir(day_path):
                        if file_name.endswith('.txt'):
                            index = int(file_name.split('.')[0])
                            date = f"{year}-{month[5:]}-{day[3:]}"
                            title = get_title(date, index, topic, n)
                            cursor.execute(f"INSERT INTO {topic} (date, idx, title) VALUES (?, ?, ?)",
                                           (date, index, title))
                    conn.commit()
                    print(day)
                print(month)
            print(year)
print('Done')
conn.close()
