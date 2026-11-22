import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    """Page Object для страницы медленного калькулятора."""

    INPUT_DELAY = (By.CSS_SELECTOR, "#delay")
    BUTTON_CALC = "//span[normalize-space()='{text}']"
    RESULT_BUTTON = (By.XPATH, "//div[@class='screen']")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу калькулятора.

        Аргументы:
            driver (WebDriver): Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    @allure.step("Открыть страницу калькулятора")
    def open_calculator_page(self) -> None:
        """Открывает веб-страницу медленного калькулятора."""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html")

    @allure.step("Установить задержку вычислений: {delay_time} сек.")
    def set_delay(self, delay_time: str) -> None:
        """Вводит время задержки перед выводом результата.

        Аргументы:
            delay_time (str): Значение задержки в секундах.
        """
        delay_input = self.driver.find_element(*self.INPUT_DELAY)
        delay_input.clear()
        delay_input.send_keys(delay_time)

    @allure.step("Нажать кнопку '{text}' на калькуляторе")
    def fill_numbers(self, text: str) -> None:
        """Нажимает на кнопку калькулятора с указанным символом.

        Аргументы:
            text (str): Текст на кнопке (цифра или математический оператор).
        """
        button_locator = (By.XPATH, self.BUTTON_CALC.format(text=text))
        edit_button = self.wait.until(
            EC.element_to_be_clickable(button_locator)
        )
        edit_button.click()

    @allure.step("Дождаться и получить результат '{expected_result}'")
    def check_form_result(self, expected_result: str) -> str:
        """Ожидает появления ожидаемого текста на экране и возвращает его.

        Аргументы:
            expected_result (str): Ожидаемый результат вычисления.

        Возврвщает:
            str: Фактический текст на экране калькулятора.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                self.RESULT_BUTTON, expected_result
            )
        )
        return self.driver.find_element(*self.RESULT_BUTTON).text
