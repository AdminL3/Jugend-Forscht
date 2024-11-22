import sqlite3
from Analysing.Plotting import graph


connection = sqlite3.connect(r"Analysing\Wordcount\wordcount.db")
cursor = connection.cursor()

name = "All"
color = "#339933"
color_reg = "#000"
topics = ["politics", "world", "opinion"]

rows = []
for topic in topics:
    cursor.execute(f"SELECT * FROM {topic};")
    rows.extend(cursor.fetchall())

columns = [column[0] for column in cursor.description]

graph(rows, columns, "wordcount", "Wordcount", "Wordcount of all three topics", ["id", "idx"],
      color, color_reg, True, 2, r"Analysing\Wordcount\output\All.png")
