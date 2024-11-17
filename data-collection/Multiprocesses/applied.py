from selenium import webdriver
import os
import multiprocessing
import time


def sleep(n):
    start_year = 2020
    amount_years = 1
    topics = ["world", "politics", "opinion"]
    start_month = n
    amount_month = 1
    last_date = 0

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_experimental_option("detach", True)
    options.add_argument("--headless")
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
                        last_date = date
                        continue

                    while True:
                        try:
                            driver.get(url)
                            page_source = driver.execute_script(
                                "return document.documentElement.outerHTML;")
                            break
                        except Exception as e:
                            print("Error: ", e)
                            time.sleep(2)
                            driver.refresh()

                    with open(output_file, "w", encoding="utf-8") as f:
                        f.write(page_source)

                    print("Saved to " + output_file)

                    last_date = date

    print("Finished saving:")
    print(f"Year {str(start_year)} to {str(start_year + amount_years - 1)}")
    print(f"Month {str(start_month)} to {str(start_month + amount_month - 1)}")
    print("and the Topics: " + str(topics))


numbers = [4, 5, 6, 7, 8, 9, 10, 11, 12]

if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        pool.map(sleep, numbers)
