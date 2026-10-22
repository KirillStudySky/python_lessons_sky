from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_edge():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 15)

    # 1. Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/
    # data-types.html в браузере Edge (если вы работаете в Windows)
    (driver.get
     ("https://bonigarcia.dev/selenium-webdriver-java/data-types.html"))

    # 2. Заполните форму значениями:
    input_first_name = wait.until(EC.presence_of_element_located(
        (By.NAME, "first-name")))
    input_first_name.send_keys("Иван")
    input_last_name = wait.until(EC.presence_of_element_located(
        (By.NAME, "last-name")))
    input_last_name.send_keys("Петров")
    input_address = wait.until(EC.presence_of_element_located(
        (By.NAME, "address")))
    input_address.send_keys("Ленина, 55-3")
    input_email = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@type='email']")))
    input_email.send_keys("test@skypro.com")
    input_phone_number = wait.until(EC.presence_of_element_located(
        (By.NAME, "phone")))
    input_phone_number.send_keys("+7985899998787")
    input_city = wait.until(EC.presence_of_element_located(
        (By.NAME, "city")))
    input_city.send_keys("Москва")
    input_country = wait.until(EC.presence_of_element_located(
        (By.NAME, "country")))
    input_country.send_keys("Россия")
    input_job_position = wait.until(EC.presence_of_element_located(
        (By.NAME, "job-position")))
    input_job_position.send_keys("QA")
    input_company = wait.until(EC.presence_of_element_located(
        (By.NAME, "company")))
    input_company.send_keys("SkyPro")

    # 3. Нажмите кнопку Submit
    submit_button = (driver.find_element
                     (By.CSS_SELECTOR, "button[type='submit']"))
    submit_button.click()

    # 4. Проверьте (assert), что поле Zip code подсвечено красным.
    zip_code_field = wait.until(EC.presence_of_element_located(
        (By.ID, "zip-code")))
    assert ("alert-danger" in zip_code_field.get_attribute
           ("class")), "Поле Zip code должно быть красным!"

    # 5. Проверьте (assert), что остальные поля подсвечены зеленым.
    green_fields_ids = [
        "first-name", "last-name", "address", "city",
        "country", "e-mail", "phone", "job-position", "company"
    ]

    for field_id in green_fields_ids:
        field = driver.find_element(By.ID, field_id)
        field_classes = field.get_attribute("class")
        assert "alert-success" in field_classes, \
            f"Поле {field_id} должно быть зеленым! Классы: {field_classes}"

    driver.quit()
