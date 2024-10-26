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

time.sleep(1)

# login
driver.get('https://x.com/signin')
user = "LeviBlu412024"
password = "X+aDGi@S484+qcL"


# benutzername
username = driver.find_element(By.TAG_NAME, 'input')
username.send_keys(user)

# click enter
button = driver.find_element(
    By.XPATH, "//button[.//span[text()='Weiter']]")
time.sleep(1)


# passwort
inputs = driver.find_elements(By.TAG_NAME, 'input')
inputs[-1].send_keys(password)


for i in range(5):
    time.sleep(1)
    print(5-i)
driver.quit()
exit
