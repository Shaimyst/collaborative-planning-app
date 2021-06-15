import os
from sys import modules
from typing import ByteString
from selenium import webdriver
import time
import pytest

# begin test

class TestLinks:
    driver = ''

    def setup_method(self):
        # open browser
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
    
    def test_home_link(self):
        home_link = self.driver.find_element_by_link_text("Home")
        home_link.click()

        self.driver.implicitly_wait(10)
        print("Current home url: " + self.driver.current_url)
        
        assert self.driver.current_url == "http://localhost/#/", "not home"

    def test_tasks_link(self):
        tasks_link = self.driver.find_element_by_link_text("Tasks")
        tasks_link.click()

        self.driver.implicitly_wait(10)

        print("Current tasks url: " + self.driver.current_url)
        
        assert self.driver.current_url == "http://localhost/#/tasks", "wrong page"

    def test_select_user(self):
        home_link = self.driver.find_element_by_link_text("Home")
        home_link.click()
        select_user_link = self.driver.find_element_by_link_text("select user")
        select_user_link.click()

        self.driver.implicitly_wait(10)

        print("Current select user url: " + self.driver.current_url)
        
        assert self.driver.current_url == "http://localhost/#/user-select", "wrong page"

    def test_create_user(self):
        home_link = self.driver.find_element_by_link_text("Home")
        home_link.click()
        select_user_link = self.driver.find_element_by_link_text("create user")
        select_user_link.click()

        self.driver.implicitly_wait(10)

        print("Current user create url: " + self.driver.current_url)
        
        assert self.driver.current_url == "http://localhost/#/user-create", "wrong page"

    def test_find_elements(self): # count the elements on a page
        home_link = self.driver.find_element_by_link_text("Home")
        home_link.click()

        count = 0

        ids = self.driver.find_elements_by_xpath('//*[@id]')
        for ii in ids:
            print("Element found: Tag name - " + ii.tag_name + ". Id attribute - " + ii.get_attribute('id'))
            count += 1 # variable will increment every loop iteration of your code

        print("Elements found: " + str(count))
        assert count == 1, "elements count has changed"

        print(dir(ii))
        

    def test_find_links(self): # lists all links on home and tasks page
        home_link = self.driver.find_element_by_link_text("Home")
        home_link.click()
        
        count = 0

        elements = self.driver.find_elements_by_xpath("//a[@href]")
        for elem in elements:
            print("Home page links: " + elem.get_attribute("href"))
            count += 1 # every loop will add one count
        
        # print("Home page links found: " + str(count))

        tasks_link = self.driver.find_element_by_link_text("Tasks")
        tasks_link.click()

        elements = self.driver.find_elements_by_xpath("//a[@href]")
        for elem in elements:
            print("Task page links: " + elem.get_attribute("href"))
            count += 1 # every loop will add one count

        print("Home and Tasks page links found: " + str(count))

        # make this one fail
        assert count == 7, "This test failed"

    def teardown_method(self):
        # close browser
        self.driver.quit()
        print("teardown initiated")