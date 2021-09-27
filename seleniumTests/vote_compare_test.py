import time
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

def test_open_tabs(browserdriver): # open 3 tabs, switch between them
    # go to specific task
    browserdriver.get('http://localhost/#/task/061c24b959994ba3be05fcd51e7cf1a3')
    browserdriver.implicitly_wait(10)
    print(browserdriver.current_url)
    assert browserdriver.current_url == "http://localhost/#/task/061c24b959994ba3be05fcd51e7cf1a3", "FAIL"

    # open a new tab
    browserdriver.execute_script("window.open('http://localhost/#/user-select', 'tab2')")
    browserdriver.switch_to.window("tab2")
    browserdriver.implicitly_wait(10)
    assert browserdriver.current_url == "http://localhost/#/user-select", "FAIL"

    # open a third tab
    browserdriver.execute_script("window.open('https://www.google.com/', 'tab3');")
    browserdriver.switch_to.window("tab3")
    browserdriver.implicitly_wait(10)
    assert browserdriver.current_url == "https://www.google.com/", "FAIL"

    # go to previous tab
    browserdriver.switch_to.window(browserdriver.window_handles[1])
    browserdriver.implicitly_wait(10)
    assert browserdriver.current_url == "http://localhost/#/user-select", "FAIL"

    # go back to main tab
    browserdriver.switch_to.window(browserdriver.window_handles[0])
    browserdriver.implicitly_wait(10)
    assert browserdriver.current_url == "http://localhost/#/task/061c24b959994ba3be05fcd51e7cf1a3", "FAIL"

def test_compare_votes(browserdriver): # votes seem to be a step behind
    # select user1
    browserdriver.get('http://localhost/#/user-select')
    browserdriver.find_element_by_xpath('/html/body/div/div[2]/ul/li[8]').click()

    # go to specific task
    browserdriver.get('http://localhost/#/task/061c24b959994ba3be05fcd51e7cf1a3')
    browserdriver.implicitly_wait(10)

    # these are the votes when you first open the page
    vote1_initial = browserdriver.find_element_by_xpath('/html/body/div/div[2]/table/tr[2]/td[2]').text
    vote3_initial = browserdriver.find_element_by_xpath('/html/body/div/div[2]/table/tr[4]/td[2]').text
    print("Before vote, Vote1 is: " + vote1_initial)
    print("Before vote, Vote3 is: " + vote3_initial)

    # select vote
    vote1 = browserdriver.find_element_by_xpath('/html/body/div/div[2]/table/tr[2]')
    vote3 = browserdriver.find_element_by_xpath('/html/body/div/div[2]/table/tr[4]')
    
    action = ActionChains(browserdriver)
        # selenium has a bug where .click() does not execute on tr or td
        # work around is importing ActionChains

    # this will select the vote on the first row, then the third row
    # (in case the third row was already selected)
    action.move_to_element(vote1).perform()
    action.click(on_element = vote1).perform()
    action.move_to_element(vote3).perform()
    action.click(on_element = vote3).perform()
    browserdriver.implicitly_wait(10)

    # these are the votes after selecting the third row vote
    vote1_aftervote = browserdriver.find_element_by_xpath('/html/body/div/div[2]/table/tr[2]/td[2]').text
    vote3_aftervote = browserdriver.find_element_by_xpath('/html/body/div/div[2]/table/tr[4]/td[2]').text
    print("Click vote3, Vote1 is: " + vote1_aftervote)
    print("Click vote3, Vote3 is: " + vote3_aftervote)

    # open a new tab
    browserdriver.execute_script("window.open('http://localhost/#/user-select', 'new tab')")
    browserdriver.implicitly_wait(10)
    # make new tab active
    browserdriver.switch_to.window(browserdriver.window_handles[-1])
    browserdriver.implicitly_wait(10)

    # select user2
    browserdriver.find_element_by_xpath('/html/body/div/div[2]/ul/li[3]').click()
    time.sleep(2)

    # go to same task
    browserdriver.get('http://localhost/#/task/061c24b959994ba3be05fcd51e7cf1a3')
    browserdriver.implicitly_wait(10)

    vote1_user2 = browserdriver.find_element_by_xpath('/html/body/div/div[2]/table/tr[2]/td[2]').text
    vote3_user2 = browserdriver.find_element_by_xpath('/html/body/div/div[2]/table/tr[4]/td[2]').text
    print("User 2, Vote1 is: " + vote1_user2)
    print("User 2, Vote3 is: " + vote3_user2)

    print("User 1 sees: " + vote3_aftervote + "User 2 sees: " + vote3_user2)


    # reinstantiate your ActionChains so element isn't using stale DOM
    # select vote in new tab

    ActionChains(browserdriver).click(browserdriver.find_element_by_xpath("/html/body/div/div[2]/table/tr[4]")).perform()
    browserdriver.implicitly_wait(10)
    time.sleep(2)

    # go back to main tab
    browserdriver.switch_to.window(browserdriver.window_handles[0])
    browserdriver.implicitly_wait(10)

    # assert votes updated 