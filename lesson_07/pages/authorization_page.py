from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthorizationPage:
    USER_NAME = (By.XPATH, "//input[@id='user-name']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN = (By.XPATH, "//input[@id='login-button']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open_shop_page(self):
        self.driver.get(
            "https://www.saucedemo.com/"
            )

    def authorization(self, user_name, password):
        edit_user_name = self.wait.until(
            EC.visibility_of_element_located(self.USER_NAME))
        edit_user_name.send_keys(user_name)
        edit_password = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD))
        edit_password.send_keys(password)
        login_btn = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN))
        login_btn.click()
