import os
import sqlite3
from Analysing.Plotting import graph

name = "All"
color = "#ff33ff"
color_reg = "#660066"
topics = ["politics", "world", "opinion"]

news = ["NYT", "Guardian"]
for new in news:
    connection = sqlite3.connect(f"Analysing/Wordcount/{new}.db")
    cursor = connection.cursor()
    rows = []
    for topic in topics:
        cursor.execute(f"SELECT * FROM {topic};")
        rows.extend(cursor.fetchall())

    columns = [column[0] for column in cursor.description]

    output = f"Output/Wordcount/Graphs/{new}/All.png"
    os.makedirs(os.path.dirname(output), exist_ok=True)
    graph(rows, columns, "wordcount", "Wordcount", "Wordcount of all topics", ["id", "idx"],
          color, color_reg, True, 2, output)
