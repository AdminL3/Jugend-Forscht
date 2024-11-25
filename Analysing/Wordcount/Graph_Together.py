import os
import sqlite3
from Analysing.Plotting import multiple


colors = ['#1f77b4', '#ff7f0e', "green"]
colors_reg = ['blue', 'red', "black"]
topics = ["Politics", "World", "Opinion"]
news = ["NYT", "Guardian"]
for n, new in enumerate(news):
    all_rows = []
    all_columns = []
    connection = sqlite3.connect(f"Analysing/Wordcount/{new}.db")
    cursor = connection.cursor()
    for i, topic in enumerate(topics):
        cursor.execute(f"SELECT * FROM {topic};")
        rows = cursor.fetchall()
        all_rows.append(rows)
        all_columns.append([column[0] for column in cursor.description])
    all_titles = ["Politics", "World", "Opinion"]
    drop_columns = ["id", "idx"]
    size = 2
    output = f"Output/Wordcount/Graphs/{new}/Together.png"
    os.makedirs(os.path.dirname(output), exist_ok=True)
    name = "wordcount"
    regression = False if new == "Guardian" else True

    multiple(all_rows, all_columns, name, all_titles, drop_columns,
             colors, colors_reg, regression, size, output)
