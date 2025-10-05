from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from selenium.common.exceptions import TimeoutException
import allure

@allure.description('''Проверка редиректов при клике на логотипы в сервисе заказа''')
@allure.description('''Тест проверяет редирект на главную страницу сервиса''')
def test_logo_scooter_redirects_home(driver):
    page = MainPage(driver)
    page.open_main()
    page.click_logo_scooter()
    assert "qa-scooter" in driver.current_url

@allure.description('''Тест проверяет редирект на главную страницу дзена''')
def test_logo_yandex_redirects_dzen(driver):
    page = MainPage(driver)
    page.open_main()
    page.click_logo_yandex()

    try:
        WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[-1])
    except TimeoutException:
        pass

    WebDriverWait(driver, 15).until(lambda d: d.current_url != "about:blank")

    assert "dzen" in driver.current_url or "yandex" in driver.current_url