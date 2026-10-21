from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    # 1. Откройте страницу https://gitflic.ru/.
    driver.get("https://gitflic.ru/")
    # 2. Установите cookie пользователя 1.
    driver.add_cookie({
        "name": "SESSION",
        "value": "Mjk3NjNjMWMtMWJmMC00OThlLTkyN2YtODYwNTdiMWRmNDAx",
        "domain": "gitflic.ru"
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
    # 3. Обновите страницу.
    driver.refresh()
    # 4. Перейдите на страницу пользователя 1
    driver.get("https://gitflic.ru/user/user1_test")
    # 5. Сохраните текущий URL.
    url_user1 = driver.current_url
    print("URL пользователя 1:", url_user1)
    # 6. Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()
    driver.get("https://gitflic.ru/")
    # 7. Установите cookie пользователя 2
    driver.add_cookie({
        "name": "SESSION",
        "value": "MTBmNWIxMzUtNjk0MC00MTFkLWJkNGQtOTU2NDZmYjkyMjNk",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
    # 8. Обновите страницу
    driver.refresh()
    # 9. Перейдите на страницу пользователя 2
    driver.get("https://gitflic.ru/user/user2_test")
    # 10. Сохраните текущий URL.
    url_user2 = driver.current_url
    print("URL пользователя 2:", url_user2)
    # 11. Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_user1 != url_user2, "URL пользователей совпадают, ошибка авторизации"
    print ("URL пользователей различны")

    driver.quit()
