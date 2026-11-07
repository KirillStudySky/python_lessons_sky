import pytest
from selenium import webdriver
from lesson_07.pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.open_calculator_page()
    calculator_page.set_delay("45")
    calculator_page.fill_numbers("7")
    calculator_page.fill_numbers("+")
    calculator_page.fill_numbers("8")
    calculator_page.fill_numbers("=")
    result = calculator_page.check_form_result(expected_result="15")
    assert result == "15", f"Ожидался результат '15', но получено '{result}'"
