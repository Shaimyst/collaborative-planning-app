import os
from selenium import webdriver
import time
import datetime

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

    date_stamp = str(datetime.datetime.now()).split('.')[0]
    file_name = "task " + date_stamp
    task_search.send_keys(file_name)

    driver.implicitly_wait(5)

    submit_button = driver.find_element_by_id("task-title-submit")
    submit_button.click()

# def test_duplicate_tasks(): # does app allow duplicate tasks to be created

def test_count_tasks(): # counts how many tasks have been created
    items = driver.find_elements_by_tag_name("li")
    count = 0

    for item in items:
        text = item.text
        count += 1
        # dupes...

    print("There are " + str(count) + " tasks.")

    # https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them
    # finds dupes in list
    # seen = {}
    # dupes = []
    #     for x in a:
    #         if x not in seen:
    #             seen[x] = 1
    #     else:
    #         if seen[x] == 1:
    #             dupes.append(x)
    #             seen[x] += 1

    # close browser
    driver.quit()
