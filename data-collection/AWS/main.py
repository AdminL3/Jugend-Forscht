from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os


start_year = 2020
amount_years = 1
topics = ["world"]
start_month = 2
amount_month = 1
last_date = 0


# Set up Chrome options
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")

# Specify the path to chromedriver
service = Service('/usr/bin/chromedriver')  # Adjust the path if necessary


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

                # Initialize the driver with Service and Options
                driver = webdriver.Chrome(service=service, options=options)
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

                page_source = driver.execute_script(
                    "return document.documentElement.outerHTML;")
                print(page_source)
                print("Continue?")
                input()
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(page_source)

                print("Saved to " + output_file)

                last_date = date
                driver.quit()


print("Finished saving:")
print(f"Year {str(start_year)} to year {str(start_year + amount_years - 1)}")
print(f"Month {str(start_month)} to month {
      str(start_month + amount_month - 1)}")
print("and Topics " + str(topics))
