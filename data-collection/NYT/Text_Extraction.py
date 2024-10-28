import os
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

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


topic = "us"

# Loop through each month and each URL
for i in range(12):
    month = i + 1
    output_dir = f"data/NYT/articles/{topic}/month{month}/"
    os.makedirs(output_dir, exist_ok=True)
    file_path = f"data/NYT/links/{topic}/month{month}.txt"
    with open(file_path, 'r', encoding='latin-1') as file:
        urls = file.read().splitlines()
    index = 0
