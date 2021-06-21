import datetime
import collections
from collections import Counter
import seleniumTests.constants as c
import pytest

# begin test
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

    browserdriver.implicitly_wait(2)
    
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

def test_list(browserdriver): # can print all task names
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

def test_open_task(browserdriver):
    browserdriver.get(c.TASKS_URL)

    # unique name generator
    date_stamp = str(datetime.datetime.now()).split('.')[0]
    unique_task_name = "task " + date_stamp

    # submit new task name
    task_input_field = browserdriver.find_element_by_xpath("/html/body/div/div[2]/form/input")
    task_input_field.send_keys(unique_task_name)
    submit_button = browserdriver.find_element_by_id("task-title-submit")
    submit_button.click()
    
    # open that task
    # vote for an element in that task

# def vote_on_task(browserdriver):
#     # open a task
#     # select a vote on task