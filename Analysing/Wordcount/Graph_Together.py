import sqlite3
from Analysing.Plotting import multiple

connection = sqlite3.connect("Analysing/Wordcount/wordcount.db")
cursor = connection.cursor()

colors = ['#1f77b4', '#ff7f0e', "green"]
colors_reg = ['blue', 'red', "black"]
topics = ["Politics", "World", "Opinion"]
all_rows = []
all_columns = []
for i, topic in enumerate(topics):
    cursor.execute(f"SELECT * FROM {topic};")
    rows = cursor.fetchall()
    all_rows.append(rows)
    all_columns.append([column[0] for column in cursor.description])
all_titles = ["Politics", "World", "Opinion"]
drop_columns = ["id", "idx"]
size = 2
output = "Analysing/Wordcount/output/Together.png"
name = "wordcount"
regression = True

multiple(all_rows, all_columns, name, all_titles, drop_columns,
         colors, colors_reg, regression, size, output)
