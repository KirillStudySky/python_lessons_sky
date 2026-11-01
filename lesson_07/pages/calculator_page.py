from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    INPUT_DELAY = (By.CSS_SELECTOR, "#delay")
    BUTTON_7 = (By.XPATH, "//span[normalize-space()='7']")
    BUTTON_PLUS = (By.XPATH, "//span[normalize-space()='+']")
    BUTTON_8 = (By.XPATH, "//span[normalize-space()='8']")
    SUBMIT_BUTTON = (By.XPATH, "//span[@class='btn btn-outline-warning']")
    RESULT_BUTTON = (By.XPATH, "//div[@class='screen']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open_calculator_page(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

    def set_delay(self):
        delay_input = self.driver.find_element(*self.INPUT_DELAY)
        delay_input.clear()
        delay_input.send_keys("45")

    def fill_numbers(self):
        edit_button_7 = self.wait.until(EC.element_to_be_clickable(
            self.BUTTON_7
        ))
        edit_button_7.click()
        edit_button_plus = self.wait.until(EC.element_to_be_clickable(
            self.BUTTON_PLUS
        ))
        edit_button_plus.click()
        edit_button_8 = self.wait.until(EC.element_to_be_clickable(
            self.BUTTON_8
        ))
        edit_button_8.click()
        edit_submit_button = self.wait.until(EC.element_to_be_clickable(
            self.SUBMIT_BUTTON
        ))
        edit_submit_button.click()

    def check_form_result(self):
        result_element = self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT_BUTTON, "15"))
        result_element = self.driver.find_element(*self.RESULT_BUTTON)
        return result_element.text
