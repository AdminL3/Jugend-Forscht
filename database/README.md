# Using a Database

- This did not work for me
- I just added this for documentation

---

### 1. Create Database for Topics

```
topics = ["politics", "world"]
for topic in topics:
     Create the table for storing article metadata
   cursor.execute(f'''
      CREATE TABLE IF NOT EXISTS {topic} (
         id INTEGER PRIMARY KEY,
         date DATE,
         idx INTEGER,
         source TEXT,
         text TEXT
      )
   ''')
```

---

### 2. Add Data thats already been created

```
def add(source, topic, filename):
    date_str = filename.split('.')[0]  # Remove the .txt extension
    date_parts = date_str.split('_')  # Split by underscore
    year = int(date_parts[0])
    month = int(date_parts[1])
    day = int(date_parts[2])
    index = int(date_parts[3])

    new_article = (f'{year}-{month}-{day}', index, content, '')

    # Insert data into the table
    cursor.execute(f'''
        INSERT INTO {topic} (date, idx, source, text)
        VALUES (?, ?, ?, ?)
    ''', new_article)
```

---

### 3. If new articles are created, add them

- Baseline on how you would do that

```
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
```
