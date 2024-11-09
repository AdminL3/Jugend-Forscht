import sqlite3
import os

conn = sqlite3.connect('database/NYT.db')
cursor = conn.cursor()


def process(source, topic, filename):
    date_str = filename.split('.')[0]  # Remove the .txt extension
    date_parts = date_str.split('_')  # Split by underscore
    year = int(date_parts[0])
    month = int(date_parts[1])
    day = int(date_parts[2])
    index = int(date_parts[3])

    new_article = (f'{year}-{month}-{day}', index, content, '')

    # Insert data into the politics table
    cursor.execute(f'''
        INSERT INTO {topic} (date, idx, source, text)
        VALUES (?, ?, ?, ?)
    ''', new_article)


output = ""

start_year = 2020
year = 0
topics = ["politics", "world"]

for topic in topics:
    # Specify the folder path
    for i in range(4):  # year
        year = start_year + i
        for k in range(12):  # month
            month = k + 1
            # Format month to always have two digits (01, 02, ..., 12)
            formatted_month = f"{month:02d}"
            folder_path = f'data/source/{topic}/{year}/month{formatted_month}'

            # Check if the folder exists before proceeding
            if os.path.exists(folder_path):
                # Loop through each file in the folder
                for filename in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, filename)

                    # Check if it's a file (not a directory)
                    if os.path.isfile(file_path):
                        try:
                            with open(file_path, 'r', encoding='utf-8') as file:
                                content = file.read()
                            print(f"Processing file: {filename}")
                            process(content, topic, filename)
                        except UnicodeDecodeError:
                            print(f"Cannot decode {filename}, skipping file.")
                            output += f"Cannot decode {
                                filename}, skipping file.\n"
            else:
                print(f"Directory {folder_path} does not exist.")
                output += f"Directory {folder_path} does not exist.\n"

conn.commit()
conn.close()

with open("database/create_results.txt", 'w', encoding='utf-8') as file:
    file.write(output)
