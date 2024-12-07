import os
import sqlite3
from Plotting.Plotting import graph


title = "All"
color = "#ff33ff"
color_reg = "#660066"
topics = ["Politics", "World", "Opinion"]
options = ['polarity', 'subjectivity']
news = ["NYT", "Guardian"]

for new in news:
    connection = sqlite3.connect(f"Database/Sentiment/{new}.db")
    cursor = connection.cursor()
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

        output = f"Output/Sentiment/{option}/{new}/{title}.png"
        os.makedirs(os.path.dirname(output), exist_ok=True)
        drop_columns = [f'{options[1-o]}', "id", "idx"]
        graph(rows, column_names, option, title1, title2,
              drop_columns, color, color_reg, regression, size, output)
