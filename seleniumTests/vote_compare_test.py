from time import sleep
import constants as c

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains

# the goal is to run the same task from 2 users
# to see if vote changes can be seen by the other in real time

# for now create a test that opens multiple tabs in the same window

def test_open_tabs(browserdriver):
    # go to specific task
    browserdriver.get('http://localhost/#/task/061c24b959994ba3be05fcd51e7cf1a3')

    browserdriver.implicitly_wait(10)

    # open a new tab
    browserdriver.execute_script("window.open('http://localhost/#/user-select', 'new tab')")

    sleep(1)

    # open a third tab
    browserdriver.execute_script("window.open('https://www.google.com');")
    sleep(1)

    # go to previous tab
    browserdriver.switch_to.window(browserdriver.window_handles[-1])

    sleep(1)

    # go back to main tab
    browserdriver.switch_to.window(browserdriver.window_handles[0])

    sleep(1)

def test_compare_votes(browserdriver):
    # select user1
    browserdriver.get('http://localhost/#/user-select')
    browserdriver.find_element_by_xpath('/html/body/div/div[2]/ul/li[8]').click()

    # go to specific task
    browserdriver.get('http://localhost/#/task/061c24b959994ba3be05fcd51e7cf1a3')
    browserdriver.implicitly_wait(10)

    # select vote
    vote1 = browserdriver.find_element_by_xpath('/html/body/div/div[2]/table/tr[2]')
    vote3 = browserdriver.find_element_by_xpath('/html/body/div/div[2]/table/tr[4]')

    action = ActionChains(browserdriver)
        # selenium has a bug where .click() does not execute on tr or td
        # work around is importing ActionChains

    # this will select the vote on the third row, then the first row
    # (in case the first row was already selected)
    action.move_to_element(vote3).perform()
    action.click(on_element = vote3).perform()
    browserdriver.implicitly_wait(10)
    action.move_to_element(vote1).perform()
    action.click(on_element=vote1).perform()
    browserdriver.implicitly_wait(10)

    # perform the operation
    # action.perform()

    # open a new tab
    browserdriver.execute_script("window.open('http://localhost/#/user-select', 'new tab')")
    browserdriver.implicitly_wait(10)
    # make new tab active
    browserdriver.switch_to.window(browserdriver.window_handles[-1])
    browserdriver.implicitly_wait(10)

    # select user2
    browserdriver.find_element_by_xpath('/html/body/div/div[2]/ul/li[3]').click()
    sleep(1)

    # go to same task
    browserdriver.get('http://localhost/#/task/061c24b959994ba3be05fcd51e7cf1a3')
    browserdriver.implicitly_wait(10)

    # select vote in new tab

    # go back to main tab
    # assert votes updated 