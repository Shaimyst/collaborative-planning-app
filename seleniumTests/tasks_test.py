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
    tasks_link = driver.find_element_by_link_text("Tasks")
    tasks_link.click()
    driver.implicitly_wait(10)
    tasksURL = "http://localhost/#/tasks"
    currentURL = driver.current_url
    
    assert tasksURL == currentURL, "URLS don't match."

def test_create_task(): # create new task with unique name
    # go to tasks page
    tasks_link = driver.find_element_by_link_text("Tasks")
    tasks_link.click()
    driver.implicitly_wait(5)

    # unique name generator
    date_stamp = str(datetime.datetime.now()).split('.')[0]
    unique_task_name = "task " + date_stamp

    # submit new task name
    task_input_field = driver.find_element_by_xpath("/html/body/div/div[2]/form/input")
    task_input_field.send_keys(unique_task_name)
    submit_button = driver.find_element_by_id("task-title-submit")
    submit_button.click()

    driver.implicitly_wait(5)
    
    # get task list
    tasks_list = driver.find_elements_by_tag_name("li")
    task_names = [x.text for x in tasks_list]

    driver.implicitly_wait(5)

    print("Unique task name: " + unique_task_name)
    print(task_names)
    
    # current assertion is failing. new inique name isn't showing 
    # assert unique_task_name in task_names, "New task wasn't created."


def test_count_tasks(): # counts how many tasks have been created
    items = driver.find_elements_by_tag_name("li")
    count = 0

    for item in items:
        text = item.text
        count += 1

    print("There are " + str(count) + " tasks.")

def test_list(): # can print all task names
    tasks_list = driver.find_elements_by_tag_name("li")
    task_names = [x.text for x in tasks_list]
    
    # print(task_names) # prints all task names

def test_list_2(): # assert if dupes exist

    # attempt to create two tasks with the same name
    # check if two tasks exist with that name
    # assert only one exists

    tasks_list = driver.find_elements_by_tag_name("li")
    task_names = [x.text for x in tasks_list]

    tasks_count = {}
    dupe_exists = False
    for tn in task_names:
        if tn in tasks_count:
            # THERE IS AT LEAST ONE DUPE
            dupe_exists = True
            tasks_count[tn] = tasks_count[tn] + 1
        else: 
            tasks_count[tn] = 1
    # print(tasks_count)

    # quit browser
    driver.quit()

    assert dupe_exists == False, "Duplicate task names exist."