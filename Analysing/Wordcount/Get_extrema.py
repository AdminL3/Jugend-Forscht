from pydoc import text
import sqlite3


def get_title(date, topic):
    parts = date.split("-")
    path = f"data/articles/{topic}/{parts[0]
                                    }/month{parts[1]}/day{parts[2]}/{parts[3]}.txt"
    with open(path, "r", encoding="utf-8") as file:
        return file.read().splitlines()[0]


def get_maxima(topic, length):
    text = ""
    connection = sqlite3.connect("Analysing/Wordcount/wordcount.db")
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {topic};")
    rows = cursor.fetchall()

    text += f"{topic.upper()}:\n\n"

    word_counts = [(row[1], row[2], row[3]) for row in rows]
    word_counts.sort(key=lambda x: x[2], reverse=True)

    for element in word_counts[:length]:
        identifier = f"{element[0]}-{element[1]}"
        title = get_title(identifier, topic)
        text += f"Date: {identifier}\nWord count: {
            element[2]}\nTitle: {title}\n\n\n"
    text += "\n"
    return text


def get_minima(topic, length):
    text = ""
    connection = sqlite3.connect("Analysing/Wordcount/wordcount.db")
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {topic};")
    rows = cursor.fetchall()

    text += f"{topic.upper()}:\n\n"

    word_counts = [(row[1], row[2], row[3]) for row in rows]
    word_counts.sort(key=lambda x: x[2])

    for element in word_counts[:length]:
        identifier = f"{element[0]}-{element[1]}"
        title = get_title(identifier, topic)
        text += f"Date: {identifier}\nWord count: {
            element[2]}\nTitle: {title}\n\n\n"
    text += "\n"
    return text


length = 1
topics = ["Politics", "World", "Opinion"]
output = "Analysing/Wordcount/output/"
options = ["Maxima", "Minima"]
for i, option in enumerate(options):
    text = f"{option}:\n\n"
    for topic in topics:
        if i == 0:
            text += get_maxima(topic.lower(), length)
        else:
            text += get_minima(topic.lower(), length)
    with open(f"{output}{option}.txt", "w", encoding="utf-8") as file:
        file.write(text)
