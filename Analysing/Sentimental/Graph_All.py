import sys
import os
import sqlite3
from Analysing.Plotting import graph

connection = sqlite3.connect("Analysing\Sentimental\sentiment.db")
cursor = connection.cursor()

title = "All"
color = "#339933"
color_reg = "#000"
topics = ["Politics", "World", "Opinion"]
options = ['polarity', 'subjectivity']

for o, option in enumerate(options):
    rows = []
    for i, topic in enumerate(topics):
        cursor.execute(f"SELECT * FROM {topic};")
        rows.extend(cursor.fetchall())

    size = 2
    regression = True
    column_names = [column[0] for column in cursor.description]
    title1 = f"{option.capitalize()} Analysis for {title}"
    title2 = option.capitalize()
    output = f"Analysing/Sentimental/output/{option}/{title}.png"
    drop_columns = [f'{options[1-o]}', "id", "idx"]
    graph(rows, column_names, option, title1, title2, drop_columns, color, color_reg, regression, size, output)
