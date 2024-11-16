import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

connection = sqlite3.connect("Analysing/Articlecount/articlecount.db")
cursor = connection.cursor()

topic_id = 0

topics = ["Politics", "World"]
topic = topics[topic_id]
colors = ['#1f77b4', '#ff7f0e']
color = colors[0] if topic == "Politics" else colors[1]


cursor.execute(f"SELECT * FROM monthly_totals WHERE topic_id = {topic_id}")
rows = cursor.fetchall()

# Create DataFrame
Dataframe = pd.DataFrame(
    rows, columns=[column[0] for column in cursor.description])

# Drop unnecessary columns
Dataframe = Dataframe.drop(columns=['id'])
Dataframe = Dataframe.drop(columns=['topic_id'])

# Combine 'year' and 'month' into a 'date' column
Dataframe['date'] = pd.to_datetime(Dataframe[['year', 'month']].assign(day=1))

# Set 'date' as the index
Dataframe.set_index('date', inplace=True)

# Plot the article counts by month
Dataframe.plot(y='total_count', style='o', markersize=4, color=color)

# Customize the plot
plt.xlabel("Date")
plt.ylabel("Article Count")
plt.legend(["Article Count"])
plt.title(f"Article Count Analysis for {topics[topic_id]}")
plt.tight_layout()

# Save the plot
plt.savefig(f"Analysing/Articlecount/output/{topics[topic_id]}.png")

plt.close()
