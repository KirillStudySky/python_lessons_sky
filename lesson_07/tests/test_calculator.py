import pytest
from selenium import webdriver
from lesson_07.pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.open_calculator_page()
    calculator_page.set_delay()
    calculator_page.fill_numbers()
    result = calculator_page.check_form_result()
    assert result == "15", f"Ожидался результат '15', но получено '{result}'"
