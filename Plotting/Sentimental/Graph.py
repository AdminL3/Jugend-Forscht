import os
import sqlite3
from Plotting.Plotting import graph

topics = ["Politics", "World", "Opinion"]
options = ['polarity', 'subjectivity']
colors = ['#1f77b4', '#ff7f0e', 'green']
colors_reg = ['blue', 'red', 'black']


news = ["NYT", "Guardian"]
for new in news:
    connection = sqlite3.connect(f"Database/Sentiment/{new}.db")
    cursor = connection.cursor()
    for o, option in enumerate(options):
        name = option.capitalize()
        drop_columns = ['id', 'idx', f'{options[1 - o]}']  # Columns to drop

        for i, topic in enumerate(topics):
            # Fetch data for the topic
            cursor.execute(f"SELECT * FROM {topic};")
            rows = cursor.fetchall()
            column_names = [col[0] for col in cursor.description]

            output = f"Output/Sentiment/{option}/{new}/{topic}.png"
            os.makedirs(os.path.dirname(output), exist_ok=True)
            # Plot using the graph function
            graph(
                rows,
                column_names,
                option,
                f"{name} for {topic}",
                f"{name} Analysis for {topic}",
                drop_columns,
                colors[i],
                colors_reg[i],
                True,
                2,
                output
            )
