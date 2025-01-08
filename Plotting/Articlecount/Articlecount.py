import os
import sqlite3
from Plotting.Plotting import graph

colors = ['#1f77b4', '#ff7f0e', "green"]
colors_reg = ['blue', 'red', "black"]
topics = ["Politics", "World", "Opinion"]
for o in ["Days", "Months"]:
    for news in ["NYT", "Guardian"]:
        connection = sqlite3.connect(f"Database/Articlecount/{o}/{news}.db")
        cursor = connection.cursor()

        for i in range(len(topics)):
            topic = topics[i]
            color = colors[i]
            regression_color = colors_reg[i]

            cursor.execute(f"SELECT * FROM {topic}")
            rows = cursor.fetchall()

            columns = [column[0] for column in cursor.description]
            output = f"Output/Articlecount/{news}/{o}/{topic}.png"
            os.makedirs(os.path.dirname(output), exist_ok=True)

            graph(rows, columns, "count", f"{topic} Articlecount", f"Articlecount of {topic}", ["id"],
                  color, regression_color, True, 2, output)
