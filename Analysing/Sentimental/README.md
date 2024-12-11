# Analysing the Sentiment ✨

Analysing the data, which we collected in [Step 1: Data Collection](../data-collection/)🗂️

## 1. Save data in Database

### 1. **Connect** to DB

```python
conn = sqlite3.connect("Analysing\Sentimental\polarity.db")
cursor = conn.cursor()
```

### 2. **Create** Table

```python
cursor.execute('''
    CREATE TABLE IF NOT EXISTS World (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        polarity INTEGER NOT NULL,
        subjectivity INTEGER NOT NULL
    )
''')
conn.commit()
```

### 3. Get **Wordcount**

```python
def get_sentiment(text):
    blob = TextBlob(text)

    # Sentiment analysis
    sentiment_polarity = blob.sentiment.polarity
    sentiment_subjectivity = blob.sentiment.subjectivity
    return [sentiment_polarity, sentiment_subjectivity]
```

### 4. **Insert** into DB

```python
cursor.executemany(
        f"INSERT INTO {topic} (date, polarity, subjectivity) VALUES (?, ?, ?)", data)
    conn.commit()
```

### 5. Close Connection

```python
conn.close()
```

---

## 2. Extracting the longest Articles

###### See my Documentation: "[Getting Extrema](../Extrema_Documentation/)"🔝

---

> [!TIP]
> Find the Table of Contents [here](https://github.com/AdminL3/Jugend-Forscht/blob/main/Table_of_contents.md)
