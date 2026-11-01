from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    USER_NAME = (By.XPATH, "//input[@id='user-name']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN = (By.XPATH, "//input[@id='login-button']")
    BUTTON_TO_ADD_BACKPACK = (
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    BUTTON_TO_ADD_T_Shirt = (
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    BUTTON_TO_ADD_Onesie = (
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
    BUTTON_BASKET = (By.XPATH, "//a[@aria-label='Cart, 3 items']")
    BUTTON_CHECKOUT = (By.XPATH, "//button[@id='checkout']")
    FIRST_NAME = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME = (By.XPATH, "//input[@id='last-name']")
    POSTAL_CODE = (By.XPATH, "//input[@id='postal-code']")
    BUTTON_CONTINUE = (By.XPATH, "//input[@id='continue']")
    TOTAL_ELEMENT = (By.XPATH, "//div[@class='summary_total_label']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 35)

    def open_shop_page(self):
        self.driver.get(
            "https://www.saucedemo.com/"
            )

    def autorization(self):
        user_name = self.wait.until(
            EC.presence_of_element_located(self.USER_NAME))
        user_name.send_keys("standard_user")
        password = self.wait.until(
            EC.presence_of_element_located(self.PASSWORD))
        password.send_keys("secret_sauce")
        login_btn = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN))
        login_btn.click()

    def basket(self):
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
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_CHECKOUT))
        checkout_button.click()

    def user_data(self):
        first_name = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_NAME))
        first_name.send_keys("Кирилл")
        last_name = self.wait.until(
            EC.element_to_be_clickable(self.LAST_NAME))
        last_name.send_keys("Гончаров")
        postal_code = self.wait.until(
            EC.element_to_be_clickable(self.POSTAL_CODE))
        postal_code.send_keys("457351")
        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_CONTINUE))
        continue_button.click()
        total_element = self.wait.until(
            EC.element_to_be_clickable(self.TOTAL_ELEMENT))
        total_element = total_element.text

    def check_total_amount(self):
        self.wait.until(
            EC.text_to_be_present_in_element(
                self.TOTAL_ELEMENT, "Total: $58.29"))
        total_element = self.driver.find_element(*self.TOTAL_ELEMENT)
        return total_element.text
