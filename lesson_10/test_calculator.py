from typing import Generator
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    """Фикстура инициализации и закрытия браузера Chrome."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка сложения чисел на медленном калькуляторе")
@allure.description(
    "Тест устанавливает задержку 45 секунд, выполняет операцию 7 + 8 "
    "и проверяет, что на экране отображается результат 15."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_form_calculator(driver: WebDriver) -> None:
    """Проверяет корректность вычисления суммы с заданной задержкой."""
    calculator_page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calculator_page.open_calculator_page()

    with allure.step("Установить задержку 45 секунд"):
        calculator_page.set_delay("45")

    with allure.step("Ввести выражение 7 + 8 ="):
        calculator_page.fill_numbers("7")
        calculator_page.fill_numbers("+")
        calculator_page.fill_numbers("8")
        calculator_page.fill_numbers("=")

    with allure.step("Проверить, что результат вычисления равен 15"):
        result = calculator_page.check_form_result(expected_result="15")
        assert result == "15", (
            f"Ожидался результат '15', но получено '{result}'"
        )
