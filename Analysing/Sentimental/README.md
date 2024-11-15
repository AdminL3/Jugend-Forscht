# Analysing the Word Count of the New York Times Articles

In previous steps we gathered all the Data from the Articles and extracted the Text, now we will analyse the Sentiment

## 1. Save data in Database

### 1. **Connect** to DB

```
conn = sqlite3.connect("Analysing\Sentimental\polarity.db")
cursor = conn.cursor()
```

### 2. **Create** Table

```
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

```
cursor.executemany(
        f"INSERT INTO {topic} (date, polarity, subjectivity) VALUES (?, ?, ?)", data)
    conn.commit()
```

#### 5. Close Connection

```
conn.close()
```

---

## 2. Visualisation in Pandas

######

###### Almost the same for Sentiment

### Differences to Wordcount

See "[Plotting the Wordcount in Pandas](https://github.com/AdminL3/Jugend-Forscht/tree/main/Analysing/Pandas_Documentation/)"
And [Analysing the Wordcount](https://github.com/AdminL3/Jugend-Forscht/tree/main/Analysing/Wordcount/)

##### Differentiate between Subjectivity and Polarity

```
sentiment_polarity = blob.sentiment.polarity
sentiment_subjectivity = blob.sentiment.subjectivity
```

##### Graphing to different plots

![Analysing Polarity](\images\polarity.png)
![Analysing Subjectivity](\images\subjectivity.png)
