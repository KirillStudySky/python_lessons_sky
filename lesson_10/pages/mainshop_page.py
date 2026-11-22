import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainShopPage:
    """Page Object для главной страницы каталога товаров Swag Labs."""

    BUTTON_TO_ADD_BACKPACK = (
        By.XPATH,
        "//button[@id='add-to-cart-sauce-labs-backpack']",
    )
    BUTTON_TO_ADD_T_Shirt = (
        By.XPATH,
        "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']",
    )
    BUTTON_TO_ADD_Onesie = (
        By.XPATH,
        "//button[@id='add-to-cart-sauce-labs-onesie']",
    )
    BUTTON_BASKET = (By.XPATH, "//a[@aria-label='Cart, 3 items']")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует главную страницу магазина.

        Аргументы:
            driver (WebDriver): Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Добавить товары в корзину")
    def add_product(self) -> None:
        """Добавляет рюкзак, футболку и комбинезон в корзину."""
        button_to_add_backpack = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_TO_ADD_BACKPACK)
        )
        button_to_add_backpack.click()

        button_to_add_t_short = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_TO_ADD_T_Shirt)
        )
        button_to_add_t_short.click()

        button_to_add_onesie = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_TO_ADD_Onesie)
        )
        button_to_add_onesie.click()

    @allure.step("Перейти в корзину")
    def open_basket(self) -> None:
        """Нажимает на иконку корзины для перехода к списку товаров."""
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_BASKET)
        ).click()
