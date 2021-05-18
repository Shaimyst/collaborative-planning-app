import os
from selenium import webdriver
import pytest
import time
import datetime

# open browser
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost/")

# all user tests

def current_milli_time():
    return round(time.time() * 1000)

def test_create_user(): # create new user
    link = driver.find_element_by_link_text("create user")
    unique_number = str(current_milli_time())
    print(link.text)
    link.click()
    driver.implicitly_wait(10)

    name_box = driver.find_element_by_xpath("/html/body/div/div[2]/form/input")
    name_box.send_keys("Profile" + unique_number)

    submit_button = driver.find_element_by_id("user-name-submit")
    submit_button.click()

def test_user_name_taken(): # duplicate user name, check error code shows
    home_link = driver.find_element_by_link_text("Home")
    home_link.click()
    link = driver.find_element_by_link_text("create user")
    link.click()

    name_box = driver.find_element_by_xpath("/html/body/div/div[2]/form/input")
    name_box.send_keys("duplicate")
    driver.implicitly_wait(5)
    submit_button = driver.find_element_by_id("user-name-submit")
    submit_button.click()
    driver.implicitly_wait(5)

    sub_error = driver.find_element_by_class_name("submission-error")
    
    assert sub_error.is_displayed(), "error message not displayed"

    # close browser
    driver.quit()