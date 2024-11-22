import sqlite3
from Analysing.Plotting import graph


connection = sqlite3.connect("Analysing/Wordcount/wordcount.db")
cursor = connection.cursor()

name = "All"
color = "#ff33ff"
color_reg = "#660066"
topics = ["politics", "world", "opinion"]

rows = []
for topic in topics:
    cursor.execute(f"SELECT * FROM {topic};")
    rows.extend(cursor.fetchall())

columns = [column[0] for column in cursor.description]

graph(rows, columns, "wordcount", "Wordcount", "Wordcount of all three topics", ["id", "idx"],
      color, color_reg, True, 2, "Analysing/Wordcount/output/All.png")
