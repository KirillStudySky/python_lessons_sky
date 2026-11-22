import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OrderPage:
    """Page Object для страницы оформления заказа Swag Labs."""

    FIRST_NAME = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME = (By.XPATH, "//input[@id='last-name']")
    POSTAL_CODE = (By.XPATH, "//input[@id='postal-code']")
    BUTTON_CONTINUE = (By.XPATH, "//input[@id='continue']")
    TOTAL_ELEMENT = (By.XPATH, "//div[@class='summary_total_label']")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу оформления заказа.

        Аргументы:
            driver (WebDriver): Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step(
        "Заполнить данные покупателя: {first_name} {last_name}, {postal_code}"
    )
    def user_data(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """Заполняет форму данных покупателя и переходит к подтверждению.

        Аргументы:
            first_name (str): Имя покупателя.
            last_name (str): Фамилия покупателя.
            postal_code (str): Почтовый индекс.
        """
        edit_first_name = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )
        edit_first_name.send_keys(first_name)

        edit_last_name = self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME)
        )
        edit_last_name.send_keys(last_name)

        edit_postal_code = self.wait.until(
            EC.visibility_of_element_located(self.POSTAL_CODE)
        )
        edit_postal_code.send_keys(postal_code)

        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_CONTINUE)
        )
        continue_button.click()

    @allure.step("Получить итоговую стоимость заказа")
    def check_total_amount(self) -> str:
        """Ожидает отображения итоговой суммы заказа и возвращает её текст.

        Возвращает:
            str: Текст элемента с итоговой стоимостью.
        """
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_ELEMENT)
        )
        return total_element.text
