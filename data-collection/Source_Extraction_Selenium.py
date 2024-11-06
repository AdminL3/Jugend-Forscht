from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import time
import pyperclip



start_year = 2020
amount_years = 1
topics = ["world"]
start_month = 2
amount_month = 2
last_date = 0




print("Do you want to login to existing session? (y/n)")

while True:
    try:
        x = input().strip().lower()
        if x == "y":
            x = True
            break
        elif x == "n":
            x = False
            break
        else:
            raise ValueError("Invalid input, please enter 'y' or 'n'.")
    except ValueError as e:
        print(e)


if x:
    pyperclip.copy(
        '"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222')
    print('Copied command to clipboard')
    input("Press any key to continue...")
    print("Accessing Session...")

    options = Options()
    options.add_experimental_option("debuggerAddress", "localhost:9222")
    driver = webdriver.Chrome(options=options)

else:
    # Setup Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_experimental_option("detach", True) 
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)


driver = webdriver.Chrome(options=options)
for topic in topics:
    for i in range(amount_years):
        year = start_year + i
        for i in range(amount_month):
            month = start_month + i
            urls_path = f"data/links/{topic}/{year}/month{month}.txt"
            with open(urls_path, 'r', encoding='utf-8') as file:
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
                
                output_dir = f"data/source/{topic}/{year}/month{month}/"
                os.makedirs(output_dir, exist_ok=True)
                output_file = os.path.join(output_dir, file_name)
                if os.path.exists(output_file):
                    print(f"File {file_name} already exists. Skipping...")
                    continue
                
                driver.get(url)

                page_source = driver.execute_script("return document.documentElement.outerHTML;")
                
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(page_source)
                
                print("Saved to " + output_file)
                    
            
                last_date = date
                
                
print("Finished saving:")
print(f"Year {str(year)} to year {str(start_year + amount_years - 1)}")
print(f"Month {str(month)} to month {str(start_month + amount_month - 1)}")
print("and Topics " + str(topics))