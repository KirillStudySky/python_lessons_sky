import pytest
from selenium import webdriver
from lesson_07.pages.shop_page import ShopPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_autorization_shop(driver):
    shop_page = ShopPage(driver)
    shop_page.open_shop_page()
    shop_page.autorization()
    shop_page.basket()
    shop_page.user_data()
    result = shop_page.check_total_amount()
    assert result == "Total: $58.29", f"Ожидался результат 'Total: $58.29', но получено '{result}'"
