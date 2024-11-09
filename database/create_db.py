import sqlite3

# Connect to the database
conn = sqlite3.connect('database/NYT.db')
cursor = conn.cursor()

topics = ["politics", "world"]
for topic in topics:
    # Create the table for storing article metadata
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {topic} (
            id INTEGER PRIMARY KEY,
            date DATE,
            idx INTEGER,
            source TEXT,
            text TEXT
        )
    ''')

# Commit and close connection
conn.commit()
conn.close()
