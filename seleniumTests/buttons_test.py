import os
from selenium import webdriver
import time

# open browser
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost/")

# begin test
def test_all_buttons():

    tags = driver.find_elements_by_tag_name('button')

    count = 0

    for t in tags:
        t.click()
        count += 1 # variable will increment every loop iteration of your code
        tagname = t.tag_name

    print(dir())

def test_links():
    home = driver.find_element_by_link_text("Home")
    home.click()

    driver.implicitly_wait(10)
    
    tasks = driver.find_element_by_link_text("Tasks")
    tasks.click()

    # close browser
    driver.quit()