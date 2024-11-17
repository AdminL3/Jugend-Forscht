# Analysing Article Count

In previous steps we gathered all the Data from the Articles and extracted the Text, now we will analyse the text

## Get Article Count

###### Create 4 new Tables

```
articles
monthly_totals
yearly_totals
topic_totals
```

inside

```python
conn = sqlite3.connect("Analysing/Articlecount/articlecount.db")
```

###### Cycle through files

###### Add to Database step by step

```python
cursor.execute("""
    INSERT INTO articles (topic_id, year, month, day, count)
    VALUES (?, ?, ?, ?, ?)
""", (topic_id, year, month, day, daily_count))
```

## Visualize

###### See "[Plotting the Wordcount in Pandas](https://github.com/AdminL3/Jugend-Forscht/tree/main/Analysing/Pandas_Documentation/)"

#### Results:
