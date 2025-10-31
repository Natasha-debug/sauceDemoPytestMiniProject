from selenium.webdriver.common.by import By

from utiles.config import URL


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = URL

    USERNAME = (By.CSS_SELECTOR, "#user-name")
    PWD = (By.CSS_SELECTOR, "#password")
    LOGINBTN = (By.CSS_SELECTOR, "#login-button")
    ERRMSG = (By.CSS_SELECTOR, ".error-message-container.error")

    def open_login_page(self):
        self.driver.get(self.url)

    def login(self, username, pwd):
        self.driver.find_element(*LoginPage.USERNAME).send_keys(username)
        self.driver.find_element(*LoginPage.PWD).send_keys(pwd)
        self.driver.find_element(*LoginPage.LOGINBTN).click()

    def get_error_msg(self):
        try:
            return self.driver.find_element(*LoginPage.ERRMSG).text
        except:
            return None
