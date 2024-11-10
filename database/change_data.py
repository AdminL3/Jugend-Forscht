import sqlite3

# Connect to the database
conn = sqlite3.connect('database/NYT.db')
cursor = conn.cursor()

# Example values for updating
date_to_update = '2024-11-09'
idx_to_update = 1
new_source = 'New Source'
new_text = 'Updated text content for the article.'

# Update the article based on date and idx
cursor.execute('''
    UPDATE politics
    SET source = ?, text = ?
    WHERE date = ? AND idx = ?
''', (new_source, new_text, date_to_update, idx_to_update))

# Commit the changes and close connection
conn.commit()
conn.close()
