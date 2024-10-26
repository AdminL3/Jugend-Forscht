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

time.sleep(2)

# accept cookies
driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()

# suche nach object
suchfeld = driver.find_element(By.CSS_SELECTOR, '[role="searchbox"]')
suchfeld.send_keys(Input)
suchbutton = driver.find_element(
    By.CSS_SELECTOR, '[data-qa="ftfind-search-submit"]')
suchbutton.click()


for i in range(5):
    time.sleep(1)
    print(5-i)
driver.quit()
exit
