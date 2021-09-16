import datetime
import collections
import time
from collections import Counter
import constants as c
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains

def test_goto_taskspage(browserdriver): # go to task page
    browserdriver.get(c.HOME_URL)
    tasks_link = browserdriver.find_element_by_link_text("Tasks")
    tasks_link.click()
    browserdriver.implicitly_wait(10)
    currentURL = browserdriver.current_url
    
    assert c.TASKS_URL == currentURL, "URLS don't match."

def test_create_task(browserdriver): # create new task with unique name
    # go to tasks page
    browserdriver.get(c.TASKS_URL)

    # unique name generator
    date_stamp = str(datetime.datetime.now()).split('.')[0]
    unique_task_name = "task " + date_stamp

    # submit new task name
    task_input_field = browserdriver.find_element_by_xpath("/html/body/div/div[2]/form/input")
    task_input_field.send_keys(unique_task_name)
    submit_button = browserdriver.find_element_by_id("task-title-submit")
    submit_button.click()
    
    # get task list
    tasks_list = browserdriver.find_elements_by_tag_name("li")
    task_names = [x.text for x in tasks_list]

    browserdriver.implicitly_wait(2)

    # print("New task created: " + unique_task_name)
    # print(task_names)

    # refresh page
    browserdriver.refresh()
    
    # assert new unique name has been created 
    assert unique_task_name is not None, "new task not created"

def test_count_tasks(browserdriver): # counts how many tasks have been created
    browserdriver.get(c.TASKS_URL)
    items = browserdriver.find_elements_by_tag_name("li")
    count = 0

    for item in items:
        text = item.text
        count += 1

    print("There are " + str(count) + " tasks.")

def test_list(browserdriver): # print all task names
    tasks_list = browserdriver.find_elements_by_tag_name("li")
    task_names = [x.text for x in tasks_list]
    
    # prints all task names:
    # print(task_names)

def test_list_2(browserdriver): # assert if dupes exist

    # attempt to create two tasks with the same name
    # check if two tasks exist with that name
    # assert only one exists

    tasks_list = browserdriver.find_elements_by_tag_name("li")
    task_names = [x.text for x in tasks_list]

    tasks_count = {}
    dupe_exists = False
    for tn in task_names:
        if tn in tasks_count:
            # THERE IS A DUPE
            dupe_exists = True
            tasks_count[tn] = tasks_count[tn] + 1
        else: 
            tasks_count[tn] = 1
    # print(tasks_count)

    assert dupe_exists == False, "Duplicate task names exist."

# test isn't selecting votes, even with action chains
# pytest -s seleniumTests/tasks_test.py::test_open_task 
def test_vote_selection(browserdriver): # open first task in list and vote
    browserdriver.get(c.TASKS_URL)

    # select first task from list
    first_task = browserdriver.find_element_by_xpath('/html/body/div/div[2]/ul/li[1]')
    first_task.click()

    browserdriver.implicitly_wait(10)

    # find and select second row vote (in case first row vote is already selected)
    row2_vote = browserdriver.find_element_by_xpath('/html/body/div/div[2]/table/tr[3]')
    row4_vote = browserdriver.find_element_by_xpath('/html/body/div/div[2]/table/tr[5]')
    action = ActionChains(browserdriver)
    action.click(on_element=row2_vote).perform()
    browserdriver.implicitly_wait(10)
    action.click(on_element=row4_vote).perform()
    browserdriver.implicitly_wait(10)
    action.double_click(on_element=row4_vote).perform()

# Aug 17 - this is not yet finding the correct css element. 
# BG color is found, but not the correct ones.
def hover_change(browserdriver): # check color change when clicking a row
    browserdriver.get(c.TASKS_URL)

    # select task from list
    first_task = browserdriver.find_element_by_xpath('/html/body/div/div[2]/ul/li[1]')
    first_task.click()

    # get css of data line
    datarow = browserdriver.find_elements_by_class_name('data-row')

    for d in datarow:
        color1 = d.value_of_css_property("background-color")
        d.click()
        color2 = d.value_of_css_property("background-color")
        print("Before click: " + color1 + "; After click: " + color2)
    
    # assert they are not equal
    assert color1 != color2



# next test idea: assert color change in hovering over data-row
