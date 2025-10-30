import pytest
from selenium import webdriver
driver = None


@pytest.fixture(scope='class')
def setup(request):
    global driver
    driver = webdriver.Chrome()
    print("\n[INFO] Launching Chrome browser...")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    #request.cls.driver = driver
    yield driver
    print("\n[INFO] Closing browser...")
    driver.quit()





    

