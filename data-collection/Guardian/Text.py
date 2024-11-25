import os
import re
from bs4 import BeautifulSoup

start_year = 2020
amount_years = 2

topics = ["politics", "world", "opinion"]


def get_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    try:
        target_div = soup.find('div', id="maincontent")
        paragraphs = target_div.find_all('p')
    except:
        return ""
    text_content = soup.title.get_text() + "\n"
    for p in paragraphs:
        text_content += p.get_text() + "\n"

    return text_content


def get_output_path(path):
    set = path.split('/')
    topic = set[3]
    filename = set[6].split(".")[0]
    date = filename.split("_")
    index = date[3]
    day = date[2]
    month = date[1]
    year = set[4]
    path = f"data/Guardian/articles/{topic}/{
        year}/month{month}/day{day}/"
    filename = f"{index}.txt"
    return [path, filename]


for topic in topics:
    print(topic)
    for i in range(amount_years):
        year = start_year + i
        print(year)
        for j in range(12):
            numbers = [str(h).zfill(2) for h in range(1, 13)]
            month = numbers[j]
            print(month)

            files_path = f"data/Guardian/source/{topic}/{year}/month{month}/"
            files = []
            if os.path.exists(files_path):
                for file in os.listdir(files_path):
                    if file.endswith('.txt'):
                        files.append(os.path.join(files_path, file))
            for file in files:
                output = get_output_path(file)
                os.makedirs(output[0], exist_ok=True)
                output_file_path = output[0] + output[1]

                if os.path.exists(output_file_path):
                    print(
                        f"File {output_file_path} already exists. Skipping...")
                    continue

                with open(file, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                article_text = get_text_from_html(html_content)
                if article_text != "":
                    # Remove the first line if it is empty
                    lines = article_text.split('\n')
                    if lines[0].strip() == '':
                        article_text = '\n'.join(lines[1:])

                    # print(output_file_path)
                    with open(output_file_path, "w", encoding="utf-8") as f:
                        f.write(article_text)
                else:
                    print(f"Error in {file}")
                    print("Skipping...")
