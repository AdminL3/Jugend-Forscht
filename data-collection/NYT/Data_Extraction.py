import time
import os
import pyperclip
from bs4 import BeautifulSoup


def clean_text(text):
    text = text.replace("SKIP ADVERTISEMENT", "")
    text = text.replace("ADVERTISEMENT", "")
    text = text.replace("Advertisement", "")
    return text
    
    
#start variables
start_year = 2020
# start_year = config.get_input_number("Input Start Year: ")
amount_years = 1
# amount_years = config.get_input_number("Input amount of years: ")

last_date = 0
topics = ["politics", "world"]
for topic in topics:
    for i in range(amount_years):
        year = start_year + i
        for j in range(12):
            numbers = [str(h).zfill(2) for h in range(1, 13)]
            month = numbers[j]
            print(month)
            files_path = f"data/NYT/source/{topic}/{year}/month{month}/"
            files = []
            print(files)
            if os.path.exists(files_path):
                for file in os.listdir(files_path):
                    if file.endswith('.txt'):
                        files.append(os.path.join(files_path, file))
            for file in files:
                with open(file, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                    
                soup = BeautifulSoup(html_content, "html.parser")

                # Find the section with name="ArticleBody"
                article_body = soup.find(attrs={"name": "articleBody"})
                title = soup.find("title").get_text()
                # Check if the section was found
                if article_body:
                    # Get the full content inside the ArticleBody tag
                    article_text = article_body.get_text(separator="\n", strip=True)
                    print("Article Body")
                    output_dir = f"data/NYT/articles/{topic}/{year}/month{month}/"
                    os.makedirs(output_dir, exist_ok=True)
                    output_file = os.path.join(output_dir, file.split('/')[-1])
                
                    with open(output_file, "w", encoding="utf-8") as f:
                        f.write(title)
                        f.write("\n"*2)
                        f.write(clean_text(article_text))
                else:
                    print("No section with name='ArticleBody' found.")
                    