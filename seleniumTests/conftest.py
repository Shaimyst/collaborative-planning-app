import pytest

@pytest.fixture
def browserdriver():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver