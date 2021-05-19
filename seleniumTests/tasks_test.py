import os
from selenium import webdriver
import time
import datetime
import collections
from collections import Counter
import pytest

# open browser
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost/")

# begin test
def test_goto_taskspage(): # go to task page
    tasks = driver.find_element_by_link_text("Tasks")
    tasks.click()
    driver.implicitly_wait(10)
    tasksURL = "http://localhost/#/tasks"
    currentURL = driver.current_url
    
    assert tasksURL == currentURL, "URLS don't match."

def test_create_task(): # create new task with unique name
    tasks = driver.find_element_by_link_text("Tasks")
    tasks.click()

    task_search = driver.find_element_by_xpath("/html/body/div/div[2]/form/input")

    date_stamp = str(datetime.datetime.now()).split('.')[0]
    file_name = "task " + date_stamp
    task_search.send_keys(file_name)

    driver.implicitly_wait(5)

    submit_button = driver.find_element_by_id("task-title-submit")
    submit_button.click()

def test_count_tasks(): # counts how many tasks have been created
    items = driver.find_elements_by_tag_name("li")
    count = 0

    for item in items:
        text = item.text
        count += 1
        # dupes...

    print("There are " + str(count) + " tasks.")

def test_list(): # works, but prints a lot of web element stuff, comment out for now.
    a = driver.find_elements_by_tag_name("li")
    task_names = [x.text for x in a]
    
    # print(task_names) # prints all task names

def test_list_2(): # UNFINISHED, it shows the counts of all task names, but we only want them printed if shown more than

    # attempt to create two tasks with the same name
    # check if two tasks exist with that name
    # assert only one exists

    a = driver.find_elements_by_tag_name("li")
    task_names = [x.text for x in a]

    task_name_to_count = {}
    dupe_exists = False
    for tn in task_names:
        if tn in task_name_to_count:
            # THERE IS AT LEAST ONE DUPE
            dupe_exists = True
            task_name_to_count[tn] = task_name_to_count[tn] + 1
        else: 
            task_name_to_count[tn] = 1
    # print(task_name_to_count)

    # quit browser
    driver.quit()

    assert dupe_exists == False, "Duplicate task names exist."
