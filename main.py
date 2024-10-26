import time
from selenium import webdriver
from selenium.webdriver.common.by import By


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

driver.get('https://x.com/home')

print("Successfully logged in!")
print("What would you like to search for?")
base_url = "https://x.com/search?q={}&src=typed_query&f=top"
# Format the URL with the search term
input = input()
url = base_url.format(input)

driver.get(url)


for i in range(5):
    time.sleep(1)
    print(5-i)
driver.quit()
exit
