import pytest
from selenium import webdriver
from lesson_07.pages.authorization_page import AuthorizationPage
from lesson_07.pages.mainshop_page import MainShopPage
from lesson_07.pages.basket_page import BasketPage
from lesson_07.pages.placing_an_order import OrderPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    authorization_page = AuthorizationPage(driver)
    authorization_page.open_shop_page()
    authorization_page.authorization("standard_user", "secret_sauce")
    main_shop = MainShopPage(driver)
    main_shop.add_product()
    basket_page = BasketPage(driver)
    basket_page.check_cart_contents()
    basket_page.checkout()
    order_page = OrderPage(driver)
    order_page.user_data("Кирилл", "Гончаров", "457351")
    result = order_page.check_total_amount()
    assert result == "Total: $58.29", (f"Ожидался результат 'Total: $58.29', "
                                       f"но получено '{result}'")
