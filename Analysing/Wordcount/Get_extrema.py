import sqlite3

topics = ["Politics", "World", "Opinion"]
for i, topic in enumerate(topics):
    print(topic)

    connection = sqlite3.connect("Analysing\Wordcount\wordcount.db")
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {topic};")
    rows = cursor.fetchall()

    with open("Analysing/Wordcount/new/wordcounts.txt", "a") as file:
        file.write(f"Wordcount for {topic}:\n\n")
        # Assuming row[0] is the day and row[1] is the word count
        word_counts = [(row[0], row[1]) for row in rows]
        word_counts.sort(key=lambda x: x[1], reverse=True)

        file.write("Top 5 days with most words:\n")
        for day, count in word_counts[:5]:
            file.write(f"Day: {day}, Word count: {count}\n")
        file.write("\n")
