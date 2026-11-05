from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage:
    BUTTON_CHECKOUT = (By.XPATH, "//button[@id='checkout']")
    SAUCE_LABS_BACKPACK = (By.XPATH, "//div[normalize-space()="
                                     "'Sauce Labs Backpack']")
    SAUCE_LABS_BOLT_T_SHIRT = (By.XPATH, "//div[normalize-space()="
                                         "'Sauce Labs Bolt T-Shirt']")
    SAUCE_LABS_ONESIE = (By.XPATH, "//div[normalize-space()="
                                   "'Sauce Labs Onesie']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def check_cart_contents(self):
        item_names = []
        for locator in [self.SAUCE_LABS_BACKPACK,
                        self.SAUCE_LABS_BOLT_T_SHIRT,
                        self.SAUCE_LABS_ONESIE]:
            items = self.driver.find_elements(*locator)
            item_names.extend([item.text for item in items])
        return item_names

    def checkout(self):
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_CHECKOUT))
        checkout_button.click()
