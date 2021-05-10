import os
from selenium import webdriver
import pytest
import time

# open browser
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost/")

# all user tests

def test_create_user(): # create new user
    link = driver.find_element_by_link_text("create user")
    print(link.text)
    link.click()
    driver.implicitly_wait(10)

    name_box = driver.find_element_by_xpath("/html/body/div/div[2]/form/input")
    name_box.send_keys("profile003")

    submit_button = driver.find_element_by_id("user-name-submit")
    submit_button.click()

    # close browser
    driver.quit()

# def select_user():

# def test_user_name_taken(): # duplicate user name, check error code shows
#     driver.get("http://localhost/#/user-create")

#     name_box = driver.find_element_by_xpath("/html/body/div/div[2]/form/input")
#     name_box.send_keys("duplicate")
#     driver.implicitly_wait(5)
#     submit_button = driver.find_element_by_id("user-name-submit")
#     submit_button.click()
#     driver.implicitly_wait(5)

#     sub_error = driver.find_element_by_class_name("submission-error")
    
#     assert sub_error.is_displayed(), "error message not displayed"

#     driver.quit()
