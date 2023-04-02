
import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Website url
URL = "https://www.python.org/"
# Chromium Drivers
# Replace path of the chromium drivers with the directory in which you have your chromium drivers 
PATH = Service('C:\Program Files (x86)\chromedriver.exe')
# i am using google chrome that's why i have webdriver.chrome option 
# You can replace it with , edge options, firefox options etc.
OP = webdriver.ChromeOptions()
DRIVER = webdriver.Chrome(service=PATH, options=OP)

#  the search keyword 
search_keyword = "cricket"
# Navigate to the website using get method 
DRIVER.get(URL)

# Find the python topbar 
top_bar = DRIVER.find_element(By.ID, 'top')

# Find all elements in the HTML List tag 
top_bar_items = top_bar.find_elements(By.TAG_NAME, 'a')

# Use for loop to iterate between the items 
for item in top_bar_items:
    print(item.text," text has the title of " ,item.get_attribute('title')) 

DRIVER.quit()