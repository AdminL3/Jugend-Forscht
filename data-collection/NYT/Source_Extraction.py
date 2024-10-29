from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


# Set up Chrome options to prevent loading extra resources (like images)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Optional: runs the browser in the background
options.add_argument('--disable-gpu')

# Initialize the WebDriver
driver = webdriver.Chrome( options=options)



#start variables
start_year = 2020
# start_year = config.get_input_number("Input Start Year: ")
amount_years = 2
# amount_years = config.get_input_number("Input amount of years: ")

last_date = 0
topics = ["politics", "world"]
for topic in topics:
    for i in range(amount_years):
        year = start_year + i
        for i in range(12):
            month = i + 1
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
                
                output_dir = f"data/NYT/source/{topic}/{year}/month{month}/"
                os.makedirs(output_dir, exist_ok=True)
                output_file = os.path.join(output_dir, file_name)
                if os.path.exists(output_file):
                    print(f"File {file_name} already exists. Skipping...")
                    continue
                
                driver.get(url)

                # Wait until the content you need is present
                try:
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME, "body"))
                    )
                    
                    # Get the complete source code as rendered by the browser
                    page_source = driver.execute_script("return document.documentElement.outerHTML;")
                    
                    # Optional: Save it to a file
                    with open(output_file, "w", encoding="utf-8") as f:
                        f.write(page_source)
                    
                    print("Source code saved successfully.")
                except Exception as e:
                    print("Error:", e)
                    
            
                last_date = date