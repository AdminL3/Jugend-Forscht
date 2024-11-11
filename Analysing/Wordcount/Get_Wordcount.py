import sqlite3
from datetime import date

# Step 1: Connect to an SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect("wordcount.db")
cursor = conn.cursor()

# Step 2: Create the table to store dates and numbers
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Wordcount (
        id INTEGER PRIMARY KEY AUTOINCREMENT,   -- unique identifier for each entry
        date TEXT NOT NULL,                     -- column to store the date in text format
        number INTEGER NOT NULL                 -- column to store the associated number
    )
''')
conn.commit()


# Get the data
sample = (str(date(2024, 11, 11)), 10)
data = []


# Step 3: Insert sample data into the table

cursor.executemany(
    "INSERT INTO DateNumbers (date, number) VALUES (?, ?)", data)
conn.commit()

# Step 4: Close the connection
conn.close()
