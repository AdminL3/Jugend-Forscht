import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

connection = sqlite3.connect("Analysing/Articlecount/articlecount.db")
cursor = connection.cursor()


topics = ["Politics", "World"]
colors = ['#1f77b4', '#ff7f0e']
for topic_id in range(2):
    topic = topics[topic_id]
    color = colors[topic_id]

    cursor.execute(f"SELECT * FROM monthly_totals WHERE topic_id = {topic_id}")
    rows = cursor.fetchall()

    # Create DataFrame
    Dataframe = pd.DataFrame(
        rows, columns=[column[0] for column in cursor.description])

    # Drop unnecessary columns
    Dataframe = Dataframe.drop(columns=['id'])
    Dataframe = Dataframe.drop(columns=['topic_id'])

    # Combine 'year' and 'month' into a 'date' column
    Dataframe['date'] = pd.to_datetime(
        Dataframe[['year', 'month']].assign(day=1))

    # Set 'date' as the index
    Dataframe.set_index('date', inplace=True)

    # Plot the article counts by month
    Dataframe.plot(y='total_count', style='o', markersize=4, color=color)

    # Customize the plot
    plt.xlabel("Date")
    plt.ylabel("Article Count")
    plt.legend([f"Article Count for {topic}"])
    plt.title(f"Monthly Analysis of Amount of Articles for {topic}")
    plt.tight_layout()

    # Save the plot
    plt.savefig(f"Analysing/Articlecount/output/month/{topic}.png")

    plt.close()
