import os
import pytest
import time
import datetime

# all user tests

def current_milli_time():
    return round(time.time() * 1000)

def test_create_user(browserdriver): # create new user
    browserdriver.get("http://localhost/")
    link = browserdriver.find_element_by_link_text("create user")
    unique_number = str(current_milli_time())
    print(link.text)
    link.click()
    browserdriver.implicitly_wait(10)

    name_box = browserdriver.find_element_by_xpath("/html/body/div/div[2]/form/input")
    name_box.send_keys("Profile" + unique_number)

    submit_button = browserdriver.find_element_by_id("user-name-submit")
    submit_button.click()

def test_user_name_taken(browserdriver): # duplicate user name, check error code shows
    home_link = browserdriver.find_element_by_link_text("Home")
    home_link.click()
    link = browserdriver.find_element_by_link_text("create user")
    link.click()

    name_box = browserdriver.find_element_by_xpath("/html/body/div/div[2]/form/input")
    name_box.send_keys("duplicate")
    browserdriver.implicitly_wait(5)
    submit_button = browserdriver.find_element_by_id("user-name-submit")
    submit_button.click()
    browserdriver.implicitly_wait(5)

    sub_error = browserdriver.find_element_by_class_name("submission-error")
    
    assert sub_error.is_displayed(), "error message not displayed"