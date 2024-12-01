import os
import sqlite3
from Plotting.Plotting import graph, multiple


topics = ["Politics", "World", "Opinion"]
options = ['polarity', 'subjectivity']
colors = ['#1f77b4', '#ff7f0e', 'green']
colors_reg = ['blue', 'red', 'black']

news = ["NYT", "Guardian"]
for new in news:
    connection = sqlite3.connect(f"Analysing/Sentimental/{new}.db")
    cursor = connection.cursor()
    for option in options:
        all_rows = []
        all_columns = []
        for topic in topics:
            cursor.execute(f"SELECT * FROM {topic};")
            rows = cursor.fetchall()
            all_rows.append(rows)
            all_columns.append([col[0] for col in cursor.description])

        output = f"Output/Sentiment/{option}/{new}/Together.png"
        os.makedirs(os.path.dirname(output), exist_ok=True)
        multiple(
            all_rows=all_rows,
            all_columns=all_columns,
            name=option,
            all_titles=topics,
            drop_columns=['id', 'idx', f'{
                options[1 - options.index(option)]}'],
            colors=colors,
            colors_reg=colors_reg,
            regression=True,
            size=2,
            output=output
        )
