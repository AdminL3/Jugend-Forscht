# Analysing the Word Count of the New York Times Articles

In previous steps we gathered all the Data from the Articles and extracted the Text, now we will analyse the Wordcount

## 1. Save data in Database

### 1. **Connect** to DB

```
conn = sqlite3.connect("Analysing\Wordcount\wordcount.db")
cursor = conn.cursor()
```

### 2. **Create** Table

```
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Wordcount (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        number INTEGER NOT NULL
    )
''')
conn.commit()
```

### 3. Get **Wordcount**

```python
def word_count(text):
    text = text.lower()
    text = text.replace("\n", " ")
    text = text.replace("  ", " ")
    text = text.replace(".", "")
    text = text.replace(",", "")
    words = text.split()
    word_count = len(words)
    return str(word_count)
```

### 4. **Insert** into DB

```
cursor.executemany(
    "INSERT INTO Wordcount (date, number) VALUES (?, ?)", data)
conn.commit()
```

#### 5. Close Connection

```
conn.close()
```

---

## 2. Visualisation in Pandas

###### See "[Plotting the Wordcount in Pandas](https://github.com/AdminL3/Jugend-Forscht/tree/main/Analysing/Pandas_Documentation/)"
