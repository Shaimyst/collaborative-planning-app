import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# open browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost/")

# begin test

def test_home_link():
    home_link = driver.find_element_by_link_text("Home")
    home_link.click()

    driver.implicitly_wait(10)
    print("Current home url: " + driver.current_url)
    
    assert driver.current_url == "http://localhost/#/", "not home"

def test_tasks_link():
    tasks_link = driver.find_element_by_link_text("Tasks")
    tasks_link.click()

    driver.implicitly_wait(10)

    print("Current tasks url: " + driver.current_url)
    
    assert driver.current_url == "http://localhost/#/tasks", "wrong page"

def test_select_user():
    home_link = driver.find_element_by_link_text("Home")
    home_link.click()
    select_user_link = driver.find_element_by_link_text("select user")
    select_user_link.click()

    driver.implicitly_wait(10)

    print("Current select user url: " + driver.current_url)
    
    assert driver.current_url == "http://localhost/#/user-select", "wrong page"

def test_create_user():
    home_link = driver.find_element_by_link_text("Home")
    home_link.click()
    select_user_link = driver.find_element_by_link_text("create user")
    select_user_link.click()

    driver.implicitly_wait(10)

    print("Current user create url: " + driver.current_url)
    
    assert driver.current_url == "http://localhost/#/user-create", "wrong page"

def test_find_elements(): # count the elements on a page
    home_link = driver.find_element_by_link_text("Home")
    home_link.click()

    count = 0

    ids = driver.find_elements_by_xpath('//*[@id]')
    for ii in ids:
        print("Element found: Tag name - " + ii.tag_name + ". Id attribute - " + ii.get_attribute('id'))
        count += 1 # variable will increment every loop iteration of your code

    print("Elements found: " + str(count))
    assert count == 1, "elements count has changed"

        #print(dir(ii))

def test_find_links(): # lists all links on home and tasks page
    home_link = driver.find_element_by_link_text("Home")
    home_link.click()
    
    count = 0

    elements = driver.find_elements_by_xpath("//a[@href]")
    for elem in elements:
        print("Home page links: " + elem.get_attribute("href"))
        count += 1 # every loop will add one count
    
    # print("Home page links found: " + str(count))

    tasks_link = driver.find_element_by_link_text("Tasks")
    tasks_link.click()

    elements = driver.find_elements_by_xpath("//a[@href]")
    for elem in elements:
        print("Task page links: " + elem.get_attribute("href"))
        count += 1 # every loop will add one count

    print("Home and Tasks page links found: " + str(count))

    assert count == 6, "wrong number of links"

    # close browser
    driver.quit()