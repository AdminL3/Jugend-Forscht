from pydoc import text
import sqlite3


def get_title(date, topic):
    parts = date.split("-")
    path = f"data/articles/{topic}/{parts[0]
                                    }/month{parts[1]}/day{parts[2]}/{parts[3]}.txt"
    with open(path, "r", encoding="utf-8") as file:
        return file.read().splitlines()[0]


def get_maxima(topic, length, option):
    option_idx = 0 if option == "polarity" else 1
    text = ""
    connection = sqlite3.connect("Analysing\Sentimental\sentiment.db")
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {topic};")
    rows = cursor.fetchall()

    text += f"{topic.upper()}:\n\n"

    variables = [(row[1], row[2], row[3], row[4]) for row in rows]

    variables.sort(key=lambda x: x[2+option_idx], reverse=True)

    for element in variables[:length]:
        identifier = f"{element[0]}-{element[1]}"
        title = get_title(identifier, topic)
        text += f"Date: {identifier}\n{option}: {
            element[2+option_idx]}\nTitle: {title}\n\n\n"
    text += "\n"
    return text


def get_minima(topic, length, option):
    option_idx = 0 if option == "polarity" else 1
    text = ""
    connection = sqlite3.connect("Analysing\Sentimental\sentiment.db")
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {topic};")
    rows = cursor.fetchall()

    text += f"{topic.upper()}:\n\n"

    variables = [(row[1], row[2], row[3], row[4]) for row in rows]

    variables.sort(key=lambda x: x[2+option_idx])

    for element in variables[:length]:
        identifier = f"{element[0]}-{element[1]}"
        title = get_title(identifier, topic)
        text += f"Date: {identifier}\n{option}: {
            element[2+option_idx]}\nTitle: {title}\n\n\n"
    text += "\n"
    return text


length = 5
topics = ["Politics", "World", "Opinion"]
types = ["Maxima", "Minima"]
options = ["polarity", "subjectivity"]
for typ in types:
    for option in options:
        output = f"Analysing/Sentimental/output/{option}/"
        text = f"{types[0]}:\n\n"
        for topic in topics:
            if typ == "Maxima":
                text += get_maxima(topic.lower(), length, option)
            else:
                text += get_minima(topic.lower(), length, option)
        with open(f"{output}{typ}.txt", "w", encoding="utf-8") as file:
            file.write(text)
