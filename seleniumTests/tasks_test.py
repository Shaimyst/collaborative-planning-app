import os
from selenium import webdriver
import time
import datetime
import collections

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
    print(task_names) # prints all task names

    # no_dupes = [x for n, x in enumerate(a) if x not in a[:n]]
    # print(no_dupes) # [[1], [2], [3], [5]]

    # dupes = [x.text for n, x in enumerate(a) if x in a[:n]]
    # print(dupes) # [[1], [3]]


# def test_list_2():
#     items = driver.find_elements_by_tag_name("li")
#     count = 0

#     for item in items:
#         text = item.text
#         count += 1

#     print(text)

    # close browser
    driver.quit()
