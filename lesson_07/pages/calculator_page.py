from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    INPUT_DELAY = (By.CSS_SELECTOR, "#delay")
    BUTTON_CALC = "//span[normalize-space()='{text}']"
    RESULT_BUTTON = (By.XPATH, "//div[@class='screen']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open_calculator_page(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html")

    def set_delay(self, delay_time):
        delay_input = self.driver.find_element(*self.INPUT_DELAY)
        delay_input.clear()
        delay_input.send_keys(delay_time)

    def fill_numbers(self, text):
        button_locator = (By.XPATH, self.BUTTON_CALC.format(text=text))
        edit_button = self.driver.find_element(*button_locator)
        edit_button.click()

    def check_form_result(self, expected_result):
        try:
            self.wait.until(EC.text_to_be_present_in_element(
                self.RESULT_BUTTON, expected_result)
            )
        except Exception:
            pass
        return self.driver.find_element(*self.RESULT_BUTTON).text
