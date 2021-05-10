import os
from selenium import webdriver
import time

# open browser
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost/")

# begin test
def test_goto_taskspage():
    tasks = driver.find_element_by_link_text("Tasks")
    tasks.click()
    driver.implicitly_wait(10)

def test_create_task():
    tasks = driver.find_element_by_link_text("Tasks")
    tasks.click()

    task_search = driver.find_element_by_xpath("/html/body/div/div[2]/form/input")
    task_search.send_keys("new task002")

    driver.implicitly_wait(5)

    submit_button = driver.find_element_by_id("task-title-submit")
    submit_button.click()

# def test_duplicate_tasks(): # does app allow duplicate tasks to be created

def test_task_list(): # get list of created tasks
    items = driver.find_elements_by_tag_name("li")
    count = 0

    for item in items:
        text = item.text
        count += 1

    print(count)
    # close browser
    driver.quit()
