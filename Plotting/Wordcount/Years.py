import os
import sqlite3
from Plotting.Plotting import graph

start_year = 2010
amount_years = 1

end_year = start_year + amount_years
colors = ['#1f77b4', '#ff7f0e', "green"]
colors_reg = ['blue', 'red', "black"]
topics = ["Politics", "World", "Opinion"]
news = ["NYT", "Guardian"]

for y in range(amount_years):
    year = start_year + y
    for n, new in enumerate(news):
        connection = sqlite3.connect(f"Database/Wordcount/{new}.db")
        cursor = connection.cursor()
        for i in range(len(topics)):
            topic = topics[i]
            color = colors[i]
            regression_color = colors_reg[i]

            cursor.execute(f'''
                           SELECT *
                            FROM {topic}
                            WHERE date >= '{year}-01-01'
                            AND date <= '{year}-12-31';
                           ''')
            rows = cursor.fetchall()

            output = f"Output/Wordcount/Graphs/{new}/{year}/{topic}.png"
            os.makedirs(os.path.dirname(output), exist_ok=True)

            columns = [column[0] for column in cursor.description]
            graph(rows, columns, "wordcount", f"{topic} Wordcount", f"Wordcount of {topic}", ["id", "idx"],
                  color, regression_color, True, 2, output)
