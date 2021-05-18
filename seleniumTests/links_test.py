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

def test_create_user():
    home = driver.find_element_by_link_text("Home")
    home.click()
    select_user = driver.find_element_by_link_text("create user")
    select_user.click()

    driver.implicitly_wait(10)

    print("Current user create url: " + driver.current_url)
    
    assert driver.current_url == "http://localhost/#/user-create", "wrong page"

def test_find_elements(): # count the elements on a page
    home = driver.find_element_by_link_text("Home")
    home.click()

    count = 0

    ids = driver.find_elements_by_xpath('//*[@id]')
    for ii in ids:
        print("tag name: " + ii.tag_name)
        print("called: " + ii.get_attribute('id'))    # id name as string
        count += 1 # variable will increment every loop iteration of your code

    print("Elements found: " + str(count))
    assert count == 1, "elements count has changed"

        #print(dir(ii))

def test_find_links(): # lists all links on home and tasks page
    home = driver.find_element_by_link_text("Home")
    home.click()
    
    count = 0

    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        print("Home page links: " + elem.get_attribute("href"))
        count += 1 # every loop will add one count
    
    # print("Home page links found: " + str(count))

    tasks = driver.find_element_by_link_text("Tasks")
    tasks.click()

    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        print("Task page links: " + elem.get_attribute("href"))
        count += 1 # every loop will add one count

    print("Home and Tasks page links found: " + str(count))

    assert count == 6, "wrong number of links"

    # close browser
    driver.quit()