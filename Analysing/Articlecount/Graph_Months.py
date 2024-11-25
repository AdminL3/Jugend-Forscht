import os
import sqlite3
from Analysing.Plotting import graph, multiple


connection = sqlite3.connect("Analysing/Articlecount/articlecount.db")
cursor = connection.cursor()

colors = ['#1f77b4', '#ff7f0e', "green"]
colors_reg = ['blue', 'red', "black"]
topics = ["Politics", "World", "Opinion"]
for i in range(len(topics)):
    topic = topics[i]
    color = colors[i]
    regression_color = colors_reg[i]

    cursor.execute(f"SELECT * FROM monthly_totals WHERE topic_id = {i}")
    rows = cursor.fetchall()

    columns = [column[0] for column in cursor.description]
    output = f"Output/Articlecount/Month/{topic}.png"
    os.makedirs(os.path.dirname(output), exist_ok=True)

    graph(rows, columns, "total_count", f"{topic} Articlecount", f"Articlecount of {topic}", ["id", "topic_id"],
          color, regression_color, True, 2, output)


# Together


all_rows = []
all_columns = []
for i, topic in enumerate(topics):
    cursor.execute(f"SELECT * FROM monthly_totals WHERE topic_id = {i}")
    rows = cursor.fetchall()
    all_rows.append(rows)
    all_columns.append([column[0] for column in cursor.description])
all_titles = ["Politics", "World", "Opinion"]
drop_columns = ["id", "topic_id"]
size = 2

output = "Output/Articlecount/Month/Together.png"
os.makedirs(os.path.dirname(output), exist_ok=True)
name = "total_count"
regression = True

multiple(all_rows, all_columns, name, all_titles, drop_columns,
         colors, colors_reg, regression, size, output)
