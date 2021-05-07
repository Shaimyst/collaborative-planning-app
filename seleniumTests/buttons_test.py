import os
from selenium import webdriver
import time

# open browser
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost/")

# begin test

def test_links():
    home = driver.find_element_by_link_text("Home")
    home.click()
    print(driver.current_url)

    driver.implicitly_wait(10)
    
    tasks = driver.find_element_by_link_text("Tasks")
    tasks.click()
    print(driver.current_url)

    driver.implicitly_wait(10)

    home.click()
    select_user = driver.find_element_by_link_text("select user")
    select_user.click()
    print(driver.current_url)

def test_find_elements():
    # count the elements on a page
    home = driver.find_element_by_link_text("Home")
    home.click()

    ids = driver.find_elements_by_xpath('//*[@id]')
    for ii in ids:
        #print ii.tag_name
        print(ii.get_attribute('id'))    # id name as string