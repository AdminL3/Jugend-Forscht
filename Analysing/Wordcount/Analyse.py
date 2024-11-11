import sqlite3
from datetime import date


conn = sqlite3.connect("wordcount.db")
cursor = conn.cursor()


# Query to get all numbers for a specific date
specific_date = "2024-11-11"
cursor.execute("SELECT number FROM DateNumbers WHERE date = ?",
               (specific_date,))
numbers_for_date = cursor.fetchall()
print(f"Numbers for {specific_date}: {numbers_for_date}")

# Query to get all dates and associated numbers
cursor.execute("SELECT date, number FROM DateNumbers ORDER BY date")
all_data = cursor.fetchall()
print("All date and number entries:")
for entry in all_data:
    print(entry)

# Query to count how many numbers are associated with each date
cursor.execute(
    "SELECT date, COUNT(number) as count_of_numbers FROM DateNumbers GROUP BY date")
count_per_date = cursor.fetchall()
print("Count of numbers per date:")
for entry in count_per_date:
    print(entry)
