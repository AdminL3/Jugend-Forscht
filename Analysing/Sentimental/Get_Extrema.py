import os
import sqlite3

from pandas import options
emojis = ["📊", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣",
          "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟",
          "1️⃣1️⃣", "1️⃣2️⃣", "1️⃣3️⃣", "1️⃣4️⃣", "1️⃣5️⃣",
          "1️⃣6️⃣", "1️⃣7️⃣", "1️⃣8️⃣", "1️⃣9️⃣", "2️⃣0️⃣"
          ]


def get_title(date, index, topic, new):
    parts = date.split("-")
    path = f"data/{new}/articles/{topic}/{parts[0]
                                          }/month{parts[1]}/day{parts[2]}/{index}.txt"
    with open(path, "r", encoding="utf-8") as file:
        return file.read().splitlines()[0]


def get_maxima(topic, length, new, o):
    conn = sqlite3.connect(f"Analysing/Sentimental/{new}.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {topic}")
    rows = cursor.fetchall()

    # Sort by word count in ascending order
    # Assuming x[3] is the word count column
    rows.sort(key=lambda x: x[3+o], reverse=True)
    bottom_articles = rows[:length]
    text = ""
    for r, row in enumerate(bottom_articles):
        date = row[1]
        word_count = row[3]
        index = row[2]
        title = get_title(date, index, topic, new)
        text += f"{emojis[r+2]}️: {date}\n"
        text += f"{title}\n"
        text += f"{options[o]}: {word_count}\n\n"

    conn.close()
    path = f"Output/Wordcount/Extrema/{new}/{options[o]}/"
    os.makedirs(path, exist_ok=True)
    with open(f"{path}Minima-{topic}.txt", "w", encoding="utf-8") as file:
        file.write(f"{emojis[0]} Bottom {length} Minima for {
                   topic.capitalize()}\n\n\n")
        file.write(text)


def get_minima(topic, length, new, o):
    conn = sqlite3.connect(f"Analysing/Sentimental/{new}.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {topic}")
    rows = cursor.fetchall()

    # Sort by word count in ascending order
    rows.sort(key=lambda x: x[3+o])  # Assuming x[3] is the word count column
    bottom_articles = rows[:length]
    text = ""
    for r, row in enumerate(bottom_articles):
        date = row[1]
        word_count = row[3]
        index = row[2]
        title = get_title(date, index, topic, new)
        text += f"{emojis[r+2]}️: {date}\n"
        text += f"{title}\n"
        text += f"{options[o]}: {word_count}\n\n"

    conn.close()
    path = f"Output/Wordcount/Extrema/{new}/{options[o]}/"
    os.makedirs(path, exist_ok=True)
    with open(f"{path}Minima-{topic}.txt", "w", encoding="utf-8") as file:
        file.write(f"{emojis[0]} Bottom {length} Minima for {
                   topic.capitalize()}\n\n\n")
        file.write(text)


length = 5
topics = ["Politics", "World", "Opinion"]
news = ["NYT", "Guardian"]
options = ["polarity", "subjectivity"]
for new in news:
    for topic in topics:
        for o in range(len(options)):
            get_maxima(topic.lower(), length, new, o)
            get_minima(topic.lower(), length, new, o)
