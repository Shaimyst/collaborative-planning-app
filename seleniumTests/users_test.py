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
    name_box.send_keys("new user")

    submit_button = driver.find_element_by_id("user-name-submit")
    submit_button.click()

# def select_user():

def test_user_name_taken():
    driver.get("http://localhost/#/user-create")

    name_box = driver.find_element_by_xpath("/html/body/div/div[2]/form/input")
    name_box.send_keys("test")
    driver.implicitly_wait(5)

    submit_button = driver.find_element_by_id("user-name-submit")
    submit_button.click()
    driver.implicitly_wait(5)

    error = driver.find_element_by_class_name("submission-error")

    if error.is_displayed():
        print("error message displayed")
    else:
        print("error message not displayed")

    driver.quit()

    # assert an error message comes up
    assert error.is_displayed(), "No error message"