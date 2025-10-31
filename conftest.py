import pytest
from utiles.driver import get_driver

driver = None


@pytest.fixture(scope='class')
def setup(request):
    global driver
    driver = get_driver()
    print("\n[INFO] Launching Chrome browser...")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    print("\n[INFO] Closing browser...")
    driver.quit()





    

