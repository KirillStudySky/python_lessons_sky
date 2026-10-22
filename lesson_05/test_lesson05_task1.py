from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/")
    driver.find_element(By.LINK_TEXT, "HTML Form").click()
    sleep(1)

    assert "/forms/post" in driver.current_url
    sleep(1)
    driver.back()
    sleep(1)
    assert "https://httpbin.qa-territory.online/" in driver.current_url
    sleep(1)

    driver.quit()
