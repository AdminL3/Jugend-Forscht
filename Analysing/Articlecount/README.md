# Analysing Article Count 📈

See overview of all Analysation Methods [here](../)

## Get Article Count

#### Create 4 new Tables

```
articles
monthly_totals
yearly_totals
topic_totals
```

#### Inside of the database

```python
conn = sqlite3.connect("Database/Articlecount/articlecount.db")
```

#### Cycle through files

- Add the files to the Database step by step

```python
cursor.execute("""
    INSERT INTO articles (topic_id, year, month, day, count)
    VALUES (?, ?, ?, ?, ?)
""", (topic_id, year, month, day, daily_count))
```

---

> [!TIP]
> Find the Table of Contents [here](https://github.com/AdminL3/Jugend-Forscht/blob/main/Table_of_contents.md)
