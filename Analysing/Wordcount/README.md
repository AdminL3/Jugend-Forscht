# Analysing the Word Count (Article Length)📏

Analysing the data, which we collected in [Step 1: Data Collection](../data-collection/)🗂️

## 1. Save data in Database

### 1. **Connect** to DB

```python
conn = sqlite3.connect("Analysing\Wordcount\wordcount.db")
cursor = conn.cursor()
```

### 2. **Create** Table

```python
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

```python
cursor.executemany(
    "INSERT INTO Wordcount (date, number) VALUES (?, ?)", data)
conn.commit()
```

#### 5. Close Connection

```python
conn.close()
```

---

## 1. Extracting the longest Articles

###### See my Documentation: "[Getting Extrema](../Extrema_Documentation/)"🔝

---

> [!TIP]
> Find the Table of Contents [here](https://github.com/AdminL3/Jugend-Forscht/blob/main/Table_of_contents.md)
