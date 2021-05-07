import os
from selenium import webdriver
import time

# open browser
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost/")

# begin test

def test_home_link():
    home = driver.find_element_by_link_text("Home")
    home.click()

    driver.implicitly_wait(10)
    print("Current home url: " + driver.current_url)
    
    assert driver.current_url == "http://localhost/#/", "not home"

def test_tasks_link():
    tasks = driver.find_element_by_link_text("Tasks")
    tasks.click()

    driver.implicitly_wait(10)

    print("Current tasks url: " + driver.current_url)
    
    assert driver.current_url == "http://localhost/#/tasks", "wrong page"

def test_select_user():
    home = driver.find_element_by_link_text("Home")
    home.click()
    select_user = driver.find_element_by_link_text("select user")
    select_user.click()

    driver.implicitly_wait(10)

    print("Current select user url: " + driver.current_url)
    
    assert driver.current_url == "http://localhost/#/user-select", "wrong page"

def test_find_elements():
    # count the elements on a page
    home = driver.find_element_by_link_text("Home")
    home.click()

    ids = driver.find_elements_by_xpath('//*[@id]')
    for ii in ids:
        #print ii.tag_name
        print(ii.get_attribute('id'))    # id name as string
        #print(dir(ii))
    
