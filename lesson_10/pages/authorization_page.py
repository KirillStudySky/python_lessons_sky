import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AuthorizationPage:
    """Page Object для страницы авторизации магазина Swag Labs."""

    USER_NAME = (By.XPATH, "//input[@id='user-name']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN = (By.XPATH, "//input[@id='login-button']")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу авторизации.

        Аргументы:
            driver (WebDriver): Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Открыть главную страницу магазина")
    def open_shop_page(self) -> None:
        """Открывает страницу входа в интернет-магазин."""
        self.driver.get("https://saucedemo.com")

    @allure.step("Авторизоваться под пользователем '{user_name}'")
    def authorization(self, user_name: str, password: str) -> None:
        """Выполняет вход в систему с указанными логином и паролем.

        Аргументы:
            user_name (str): Имя пользователя.
            password (str): Пароль пользователя.
        """
        edit_user_name = self.wait.until(
            EC.visibility_of_element_located(self.USER_NAME)
        )
        edit_user_name.send_keys(user_name)

        edit_password = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        edit_password.send_keys(password)

        login_btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN))
        login_btn.click()
