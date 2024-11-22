import sqlite3
from Analysing.Plotting import graph

connection = sqlite3.connect("Analysing\Wordcount\wordcount.db")
cursor = connection.cursor()

colors = ['#1f77b4', '#ff7f0e', "green"]
colors_reg = ['blue', 'red', "black"]
topics = ["Politics", "World", "Opinion"]

for i in range(len(topics)):
    topic = topics[i]
    color = colors[i]
    regression_color = colors_reg[i]

    cursor.execute(f"SELECT * FROM {topic};")
    rows = cursor.fetchall()

    columns = [column[0] for column in cursor.description]

    graph(rows, columns, "wordcount", f"{topic} Wordcount", f"Wordcount of {topic}", ["id", "idx"],
                    color, regression_color, True, 2, f"Analysing\Wordcount\output\{topic}.png")
