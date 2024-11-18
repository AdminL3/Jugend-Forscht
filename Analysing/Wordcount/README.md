# Analysing the Word Count of the New York Times Articles

In previous steps we gathered all the Data from the Articles and extracted the Text, now we will analyse the Wordcount

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

## 2. Visualisation in Pandas

###### See my Documentation: "[Plotting the Wordcount in Pandas](../Pandas_Documentation/)"

## 3. Extracting the longest Articles

###### See my Documentation: "[Getting Extrema](../Extrema_Documentation/)"

Output:
```
Maxima:

POLITICS:

Date: 2021-01-06-24
Word count: 11912
Title: Protestors clashed with police outside of the Capitol on Wednesday.

...
```