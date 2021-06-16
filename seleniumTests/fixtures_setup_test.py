import os
from sys import modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

# this test uses fixtures to open and close a browser per function
# begin test

class TestLinks:
    driver = ''

    def setup_method(self):
        # open browser
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://google.com")

    # def search_bar(self):
    #     search_bar = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    
    def test_search_cats(self):
        # accept cookies
        cookies_button = self.driver.find_element_by_id("L2AGLb")
        cookies_button.click()
        # find search bar and input search
        search_bar = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        search_bar.send_keys("cat images")
        # find and click submit button
        submit_button = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
        submit_button.submit()

        assert self.driver.current_url != "http://google.com", "didn't search for cats"

    def test_search_wolves(self):
        # accept cookies
        search_bar = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        cookies_button = self.driver.find_element_by_id("L2AGLb")
        cookies_button.click()
        # find search bar and input search
        search_bar.send_keys("wolves images")
        # find and click submit button
        submit_button = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
        submit_button.submit()

        assert self.driver.current_url != "http://google.com", "something is wrong"

    def teardown_method(self):
        # close browser
        self.driver.quit()
        print("teardown initiated")