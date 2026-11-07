from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainShopPage:
    BUTTON_TO_ADD_BACKPACK = (
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    BUTTON_TO_ADD_T_Shirt = (
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    BUTTON_TO_ADD_Onesie = (
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
    BUTTON_BASKET = (By.XPATH, "//a[@aria-label='Cart, 3 items']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def add_product(self):
        button_to_add_backpack = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_TO_ADD_BACKPACK))
        button_to_add_backpack.click()
        button_to_add_t_short = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_TO_ADD_T_Shirt))
        button_to_add_t_short.click()
        button_to_add_onesie = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_TO_ADD_Onesie))
        button_to_add_onesie.click()
        basket_button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_BASKET))
        basket_button.click()
