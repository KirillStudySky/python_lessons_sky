from typing import Generator
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from pages.authorization_page import AuthorizationPage
from pages.basket_page import BasketPage
from pages.mainshop_page import MainShopPage
from pages.placing_an_order import OrderPage


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    """Фикстура инициализации и закрытия браузера Firefox."""
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка оформления заказа в интернет-магазине Swag Labs")
@allure.description(
    "Тест выполняет авторизацию, добавляет 3 товара в корзину, проверяет "
    "содержимое корзины, заполняет данные покупателя и сверяет итоговую сумму."
)
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver: WebDriver) -> None:
    """Проверяет полный сценарий покупки трёх товаров в магазине."""
    authorization_page = AuthorizationPage(driver)

    with allure.step("Открыть магазин и авторизоваться"):
        authorization_page.open_shop_page()
        authorization_page.authorization("standard_user", "secret_sauce")

    main_shop = MainShopPage(driver)

    with allure.step("Добавить товары в корзину и перейти в неё"):
        main_shop.add_product()
        main_shop.open_basket()

    basket_page = BasketPage(driver)

    with allure.step("Проверить список товаров в корзине"):
        cart_items = basket_page.check_cart_contents()
        expected_items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]
        assert cart_items == expected_items, (
            f"Ожидались товары {expected_items}, но получены {cart_items}"
        )

    with allure.step("Перейти к оформлению заказа"):
        basket_page.checkout()

    order_page = OrderPage(driver)

    with allure.step("Заполнить данные покупателя"):
        order_page.user_data("Кирилл", "Гончаров", "457351")

    with allure.step("Проверить итоговую сумму заказа"):
        result = order_page.check_total_amount()
        assert result == "Total: $58.29", (
            f"Ожидался результат 'Total: $58.29', но получено '{result}'"
        )
