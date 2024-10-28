import os
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import config


# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-search-engine-choice-screen")
options.add_experimental_option("detach", True) 
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Go to Google to initialize driver
driver.get('https://google.com/')
print(driver.title)


last_date = 0
year = 2020
# year = config.get_input_number("What year do you want to convert?")
topics = config.topics
for topic in topics:
    for i in range(12):
        month = i + 1
        output_dir = f"data/NYT/articles/{topic}/{year}/month{month}/"
        os.makedirs(output_dir, exist_ok=True)
        urls_path = f"data/NYT/links/{topic}/{year}/month{month}.txt"
        with open(urls_path, 'r', encoding='latin-1') as file:
            urls = file.read().splitlines()
        index = 0
        for url in urls:
            parts = url.split('/')
            year = parts[3]
            month = parts[4]
            day = parts[5]
            date = f"{year}_{month}_{day}_"
            if last_date == date:
                index += 1
            else:
                index = 1
            file_name = f"{date}{index}.txt"
            
            output_file = os.path.join(output_dir, file_name)
            if os.path.exists(output_file):
                print(f"File {file_name} already exists. Skipping...")
                continue
            
            print("Getting source code for URL:", url)
            driver.get(url)
            
            soup = BeautifulSoup(driver.page_source, "html.parser")
            
            article_section = soup.find("section", {"name": "articleBody"})
            
            if article_section:
                print("Article body found.")
                # Extract all text from paragraph tags inside the divs
                paragraphs = article_section.find_all("p")
                article_text = "\n".join([p.get_text() for p in paragraphs])

                # Write article text to a file
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(article_text)
        
            last_date = date