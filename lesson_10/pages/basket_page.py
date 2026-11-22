import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasketPage:
    """Page Object для страницы корзины покупок Swag Labs."""

    BUTTON_CHECKOUT = (By.XPATH, "//button[@id='checkout']")
    SAUCE_LABS_BACKPACK = (
        By.XPATH,
        "//div[normalize-space()='Sauce Labs Backpack']",
    )
    SAUCE_LABS_BOLT_T_SHIRT = (
        By.XPATH,
        "//div[normalize-space()='Sauce Labs Bolt T-Shirt']",
    )
    SAUCE_LABS_ONESIE = (
        By.XPATH,
        "//div[normalize-space()='Sauce Labs Onesie']",
    )

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу корзины.

        Аргументы:
            driver (WebDriver): Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Получить список названий товаров в корзине")
    def check_cart_contents(self) -> list[str]:
        """Собирает названия добавленных товаров на странице корзины.

        Врзвращает:
            list[str]: Список названий товаров, найденных в корзине.
        """
        item_names: list[str] = []
        for locator in [
            self.SAUCE_LABS_BACKPACK,
            self.SAUCE_LABS_BOLT_T_SHIRT,
            self.SAUCE_LABS_ONESIE,
        ]:
            items = self.driver.find_elements(*locator)
            item_names.extend([item.text for item in items])
        return item_names

    @allure.step("Нажать кнопку Checkout для оформления заказа")
    def checkout(self) -> None:
        """Переходит к оформлению заказа."""
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_CHECKOUT)
        )
        checkout_button.click()
