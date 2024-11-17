from os import path
import sqlite3


def get_title(date, topic):
    parts = date.split("-")

    topic = "Politics"
    path = f"data/articles/{topic}/{parts[0]
                                    }/month{parts[1]}/day{parts[2]}/{parts[3]}.txt"
    with open(path, "r", encoding="utf-8") as file:
        return (file.read().splitlines()[0])


def get_extrema(topic):
    text = ""
    connection = sqlite3.connect("Analysing\Wordcount\wordcount.db")
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {topic};")
    rows = cursor.fetchall()

    text += f"{topic}:\nTop 5:\n\n"
    text += ""

    word_counts = [(row[1], row[2], row[3]) for row in rows]
    word_counts.sort(key=lambda x: x[2], reverse=True)

    for element in word_counts[:5]:
        identifier = f"{element[0]}-{element[1]}"
        title = get_title(identifier, topic)
        text += f"Date: {identifier}\nWord count: {
            element[2]}\nTitle: {title}\n\n\n"
    text += "\n"
    return text


topics = ["Politics", "World", "Opinion"]
output = "Analysing/Wordcount/extrema.txt"
with open(output, "w") as file:
    file.write("Wordcount analysis\n\n")
with open(output, "a") as file:
    for i, topic in enumerate(topics):
        file.write(get_extrema(topic))
