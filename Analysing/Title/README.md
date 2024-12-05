# Saving Article Titles to SQLite Database

## 1. Import necessary modules:

- `os` for interacting with the operating system.
- `sqlite3` for interacting with SQLite databases.

## 2. Define the `get_title` function:

- Parameters:
  - `date`: A string representing the date in the format "YYYY-MM-DD".
  - `index`: An integer representing the index of the article.
  - `topic`: A string representing the topic of the article.
  - `new`: A string representing the news source.
- Functionality:
  - Splits the `date` string into year, month, and day.
  - Constructs the file path based on the provided parameters.
  - Opens the file at the constructed path and reads the first line, which is assumed to be the title of the article.
  - Returns the title of the article.

## 3. Initialize variables:

- `base_path`: A string representing the base directory where data is stored.
- `topics`: A list of strings representing different topics.
- `news`: A list of strings representing different news sources.

## 4. Iterate over each news source in `news`:

- Construct the path to the SQLite database for the current news source.
- Connect to the SQLite database.
- Create a cursor object to execute SQL commands.

## 5. Iterate over each topic in `topics`:

- Create a table for the current topic if it does not already exist. The table has columns for `date`, `index`, and `title`.

## 6. Iterate over the directory structure to find article files:

- Construct the path to the directory for the current topic.
- Iterate over each year directory within the topic directory.
- Iterate over each month directory within the year directory.
- Iterate over each day directory within the month directory.
- Iterate over each file within the day directory.

## 7.For each file:

- Check if the file has a `.txt` extension.
- Extract the index from the file name.
- Construct the date string from the year, month, and day.
- Call the `get_title` function to get the title of the article.
- Insert the date, index, and title into the corresponding table in the SQLite database.
- Commit the transaction to save the changes.
