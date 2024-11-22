import sqlite3
from Analysing.Plotting import graph, multiple


# Database connection
connection = sqlite3.connect("Analysing/Sentimental/sentiment.db")
cursor = connection.cursor()

# Settings
topics = ["Politics", "World", "Opinion"]
options = ['polarity', 'subjectivity']
colors = ['#1f77b4', '#ff7f0e', 'green']
colors_reg = ['blue', 'red', 'black']



for o, option in enumerate(options):
    name = option.capitalize()
    drop_columns = ['id', 'idx', f'{options[1 - o]}']  # Columns to drop

    for i, topic in enumerate(topics):
        # Fetch data for the topic
        cursor.execute(f"SELECT * FROM {topic};")
        rows = cursor.fetchall()
        column_names = [col[0] for col in cursor.description]

        # Plot using the graph function
        graph(
            rows=rows,
            column_names=column_names,
            name=option,
            title1=f"{name} for {topic}",
            title2=f"{name} Analysis for {topic}",
            drop_columns=drop_columns,
            color=colors[i],
            color_reg=colors_reg[i],
            regression=True,
            size=2,
            output=f"Analysing/Sentimental/output/{option}/{topic}.png"
        )