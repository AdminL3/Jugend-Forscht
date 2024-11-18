# Documentation for Word Count Analysis Script

This script analyzes word counts from an SQLite database, identifies the maximum and minimum word counts for given topics, and generates text files summarizing the results. The script also retrieves article titles from a directory structure based on the provided date and topic.

---

## Functions

### `get_maxima/minima(topic, length)`

**Description**: Fetches articles with the highest/lowest word counts for a given topic.

**Access Database**:

```python
connection = sqlite3.connect("Analysing/Wordcount/wordcount.db")
cursor = connection.cursor()

cursor.execute(f"SELECT * FROM {topic};")
rows = cursor.fetchall()
```

**Save important information**:

- (index, date, date-idx, word_count) for each row.
- We only need date and idx for the title.
- And word_count for sorting.

```python
word_counts = [(row[1], row[2], row[3]) for row in rows]
```

**Sort**:

- Sort after new index two, which is old index 3 which is the word count

```python
word_counts.sort(key=lambda x: x[2], reverse=True)`
```

**Output the top `length` articles**:

```python
    for element in word_counts[:length]:
```

---

### `get_title(date, topic)`

**Description**: Retrieves the title of an article based on its date and topic.

**Parameters**:

- `date` (str): Date in the format `YYYY-MM-DD-index`.
- `topic` (str): Article topic (e.g., "politics").

**Returns**: Title of the article.

**Example**:

```python
title = get_title("2023-11-01-1", "politics")
```

---

## Workflow

1. **Define Topics and Options**:

   - Topics: `["Politics", "World", "Opinion"]`
   - Options: `["Maxima", "Minima"]`

2. **Fetch and Process Data**:

   - For each topic, retrieve word counts from the database.
   - Sort the word counts in descending order (for maxima) or ascending order (for minima).

3. **Retrieve Titles**:

   - Use `get_title()` to fetch article titles based on the `YYYY-MM-DD-index` format.

4. **Generate Output**:
   - Write summaries of maxima and minima to separate text files in the `output` directory.

---

## Output

### Maxima Output

File: `Analysing/Wordcount/output/Maxima.txt`

**Example**:

```
Maxima:

POLITICS:

Date: 2021-01-06-24
Word count: 11912
Title: Protestors clashed with police outside of the Capitol on Wednesday.

...

WORLD:

Date: 2020-07-09-5
Word count: 11488
Title: U.S. Hits Another Record for New Coronavirus Cases

...

OPINION:

Date: 2020-10-15-3
Word count: 11635
Title: Can Big Tech Make Sure That 2020 Is Not 2016?

...
```

## Full code for other projects

```python
def get_title(date, topic):
   parts = date.split("-")
   path = f"data/articles/{topic}/{parts[0]}/month{parts[1]}/day{parts[2]}/{parts[3]}.txt"
   with open(path, "r", encoding="utf-8") as file:
      return file.read().splitlines()[0]
```

```python
def get_maxima(topic, length):
text = ""
connection = sqlite3.connect("Analysing/Wordcount/wordcount.db")
cursor = connection.cursor()

cursor.execute(f"SELECT * FROM {topic};")
rows = cursor.fetchall()

text += f"{topic.upper()}:\n\n"

word_counts = [(row[1], row[2], row[3]) for row in rows]
word_counts.sort(key=lambda x: x[2], reverse=True)

for element in word_counts[:length]:
   identifier = f"{element[0]}-{element[1]}"
   title = get_title(identifier, topic)
   text += f"Date: {identifier}\nWord count: {
      element[2]}\nTitle: {title}\n\n\n"
text += "\n"
return text
```

```python
length = 5
topics = ["Politics", "World", "Opinion"]
output = "Analysing/Wordcount/output/"
options = ["Maxima", "Minima"]
for i, option in enumerate(options):
   text = f"{option}:\n\n"
   for topic in topics:
      if i == 0:
        text += get_maxima(topic.lower(), length)
      else:
         text += get_minima(topic.lower(), length)
      with open(f"{output}{option}.txt", "w", encoding="utf-8") as file:
         file.write(text)
```
