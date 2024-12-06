import os
import re

start_year = 2010
amount_years = 1

topics = ["politics", "world", "opinion"]


def get_text_from_html(html):
    matches = re.findall(r'"text":"(.*?)"', html)
    matches = list(dict.fromkeys(matches))
    text = ""
    for match in matches:
        text += match + "\n"

    return text


def get_output_path(path):
    set = path.split(r'/')
    topic = set[3]
    filename = set[6].split(".")[0]
    date = filename.split("_")
    index = date[3]
    day = date[2]
    month = date[1]
    year = set[4]
    return [f"data/NYT/articles/{topic}/{year}/month{month}/day{day}/", f"{index}.txt"]


for topic in topics:
    print(topic)
    for i in range(amount_years):
        year = start_year + i
        print(year)
        for j in range(12):
            numbers = [str(h).zfill(2) for h in range(1, 13)]
            month = numbers[j]
            print(month)
            files_path = f"data/NYT/source/{topic}/{year}/month{month}/"
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
                    # print(
                    # f"File {output_file_path} already exists. Skipping...")
                    continue

                with open(file, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                article_text = get_text_from_html(html_content)

                # Remove the first line if it is empty
                lines = article_text.split('\n')
                if lines[0].strip() == '':
                    article_text = '\n'.join(lines[1:])
                print("Writing to file:", output_file_path)
                with open(output_file_path, "w", encoding="utf-8") as f:
                    f.write(article_text)
