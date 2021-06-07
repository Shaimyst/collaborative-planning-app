from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

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

if __name__ == "__main__":
    unittest.main()