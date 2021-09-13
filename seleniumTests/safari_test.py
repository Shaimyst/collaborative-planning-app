from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import constants as c

# this is a test to open the local host in safari

def setup_module(module):
    WebKitFeatureStatusTest.driver = webdriver.Safari()

def teardown_module(module):
    WebKitFeatureStatusTest.driver.quit()

class WebKitFeatureStatusTest(unittest.TestCase):
    
    def test_feature_status_page_search_safari(self):
        self.driver.get("http://localhost/")
        create_user_link = self.driver.find_element_by_link_text("create user")
        create_user_link.click()

    def test_home_link_safari(self): # test Home link works
        self.driver.get(c.HOME_URL)
        home_link = self.driver.find_element_by_link_text("Home")
        home_link.click()

        self.driver.implicitly_wait(10)
        print("Current home url: " + self.driver.current_url)
    
        assert self.driver.current_url == c.HOME_URL, "not home"

    def test_tasks_link_safari(self): # test tasks link works
        self.driver.get(c.HOME_URL)
        tasks_link = self.driver.find_element_by_link_text("Tasks")
        tasks_link.click()

        self.driver.implicitly_wait(10)

        print("Current tasks url: " + self.driver.current_url)
        
        assert self.driver.current_url == c.TASKS_URL, "wrong page"

if __name__ == "__main__":
    unittest.main()