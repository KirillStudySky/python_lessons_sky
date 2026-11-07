from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    FIRST_NAME = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME = (By.XPATH, "//input[@id='last-name']")
    POSTAL_CODE = (By.XPATH, "//input[@id='postal-code']")
    BUTTON_CONTINUE = (By.XPATH, "//input[@id='continue']")
    TOTAL_ELEMENT = (By.XPATH, "//div[@class='summary_total_label']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def user_data(self, first_name, last_name, postal_code):
        edit_first_name = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME))
        edit_first_name.send_keys(first_name)
        edit_last_name = self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME))
        edit_last_name.send_keys(last_name)
        edit_postal_code = self.wait.until(
            EC.visibility_of_element_located(self.POSTAL_CODE))
        edit_postal_code.send_keys(postal_code)
        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_CONTINUE))
        continue_button.click()

    def check_total_amount(self):
        total_element = self.wait.until(EC.visibility_of_element_located(
            self.TOTAL_ELEMENT))
        return total_element.text
