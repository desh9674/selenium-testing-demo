from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.lgn_btn = (By.ID, "login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, user):
        self.driver.find_element(*self.username).send_keys(user)
    
    def enter_password(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.lgn_btn).click()


