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
