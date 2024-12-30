import os
import sqlite3
emojis = ["📊", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣",
          "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟",
          "1️⃣1️⃣", "1️⃣2️⃣", "1️⃣3️⃣", "1️⃣4️⃣", "1️⃣5️⃣",
          "1️⃣6️⃣", "1️⃣7️⃣", "1️⃣8️⃣", "1️⃣9️⃣", "2️⃣0️⃣"
          ]


def get_extrema(topic, length, new, typ):
    conn = sqlite3.connect(f"Database/Articlecount/Days/{new}.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {topic}")
    rows = cursor.fetchall()

    rows.sort(key=lambda x: x[2], reverse=True if typ == 0 else False)
    top_articles = rows[:length]
    text = ""
    for r, row in enumerate(top_articles):
        date = row[1]
        word_count = row[2]
        text += f"{emojis[r+1]}️: {date}\n"
        text += f"Articlecount: {word_count}\n\n"

    conn.close()
    path = f"Output/Articlecount/Extrema/{new}/"
    os.makedirs(path, exist_ok=True)
    with open(f"{path}{typen[typ]}-{topic}.txt", "w", encoding="utf-8") as file:
        file.write(f"{emojis[0]} Top {length} {typen[typ]} for {
                   topic.capitalize()}\n\n\n")
        file.write(text)


length = 5
topics = ["Politics", "World", "Opinion"]
news = ["NYT", "Guardian"]
typen = ["Maxima", "Minima"]
for new in news:
    for topic in topics:
        for i in range(len(typen)):
            get_extrema(topic.lower(), length, new, i)
