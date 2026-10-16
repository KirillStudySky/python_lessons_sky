from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Кирилл Гончаров")
    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit order']")
    submit_button.click()
    assert "https://httpbin.qa-territory.online/post" in driver.current_url

    driver.quit()
