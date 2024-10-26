import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

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
    print('You are expected to have all prior steps done as explained in the README!')
    pyperclip.copy(
        '"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222')
    print('Copied command to clipboard')
    input("Press any key to continue...")
    options = Options()
    options.add_experimental_option("debuggerAddress", "localhost:9222")
    driver = webdriver.Chrome(options=options)


else:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    driver.get('https://x.com/home')
    print(driver.title)

    time.sleep(3)

    # accept all cookies
    button = driver.find_element(
        By.XPATH, "//button[.//span[text()='Alle Cookies akzeptieren']]")
    button.click()

    # login
    driver.get('https://x.com/signin')
    user = "LeviBlu412024"
    password = "X+aDGi@S484+qcL"
    email = "l-blu@outlook.de"

    time.sleep(3)

    # benutzername
    username = driver.find_element(By.TAG_NAME, 'input')
    username.send_keys(user)

    # click enter
    driver.find_element(By.XPATH, "//span[text()='Weiter']").click()
    time.sleep(2)

    inputs = driver.find_elements(By.TAG_NAME, 'input')
    try:
        verification = driver.find_element(
            By.XPATH, "//span[text()='Gib deine Telefonnummer oder E-Mail-Adresse ein']")
        inputs[-1].send_keys(email)
        driver.find_element(By.XPATH, "//span[text()='Weiter']").click()
    except:
        pass

    time.sleep(1)
    inputs = driver.find_elements(By.TAG_NAME, 'input')
    # passwort
    inputs[-1].send_keys(password)

    # click login
    driver.find_element(By.XPATH, "//span[text()='Anmelden']").click()
    time.sleep(2)

    # go home

    print("Successfully logged in!")

print("Successfully logged in!")
driver.get('https://x.com/home')
# search function
print("What would you like to search for?")
base_url = "https://x.com/search?q={}&src=typed_query&f=top"

topic = input()

amount = 5
print(f"Taking first {amount} articles")


url = base_url.format(topic)
driver.get(url)
time.sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
articles = driver.find_elements(By.TAG_NAME, 'article')
print(f"There are {len(articles)} articles found")
while True:
    print("How many do you want to extract?")
    amount = input()
    try:
        int(amount)
        break
    except:
        print("Not a number, try again:")

urls = []
for i in range(amount):
    article = articles[i]
    a_tag = article.find_element(By.TAG_NAME, 'a')
    url = a_tag.get_attribute('href')
    urls.append(url)
