from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # 1. Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/
    # slow-calculator.html в Google Chrome.
    (driver.get
     ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"))

    # 2. В поле ввода по локатору # delay введите значение 45.
    input_delay = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#delay")))
    input_delay.clear()
    input_delay.send_keys("45")

    # 3.Нажмите на кнопки:
    submit_button_7 = driver.find_element(
        By.XPATH, "//span[normalize-space()='7']")
    submit_button_7.click()
    submit_button = driver.find_element(
        By.XPATH, "//span[normalize-space()='+']")
    submit_button.click()
    submit_button_8 = driver.find_element(
        By.XPATH, "//span[normalize-space()='8']")
    submit_button_8.click()
    submit_button_ = driver.find_element(
        By.XPATH, "//span[@class='btn btn-outline-warning']")
    submit_button_.click()

    # 4. Проверьте (assert), что в окне отобразится
    # результат 15 через 45 секунд.
    result_element = WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.XPATH, "//div[@class='screen']"),"15")
    ), "Результат 15 через 45 секунд"
    assert result_element, "Результат не равен 15"

    driver.quit()
