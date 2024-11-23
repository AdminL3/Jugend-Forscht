import os
import sqlite3
from Analysing.Plotting import graph


colors = ['#1f77b4', '#ff7f0e', "green"]
colors_reg = ['blue', 'red', "black"]
topics = ["Politics", "World", "Opinion"]

news = ["NYT", "Guardian"]
for n, new in enumerate(news):
    connection = sqlite3.connect(f"Analysing/Wordcount/{new}.db")
    cursor = connection.cursor()
    for i in range(len(topics)):
        topic = topics[i]
        color = colors[i]
        regression_color = colors_reg[i]

        cursor.execute(f"SELECT * FROM {topic};")
        rows = cursor.fetchall()

        output = f"Output/Wordcount/Graphs/{new}/{topic}.png"
        os.makedirs(os.path.dirname(output), exist_ok=True)

        columns = [column[0] for column in cursor.description]
        graph(rows, columns, "wordcount", f"{topic} Wordcount", f"Wordcount of {topic}", ["id", "idx"],
              color, regression_color, True, 2, output)
