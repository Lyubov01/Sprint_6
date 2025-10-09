from pages.main_page import MainPage
import allure
from data import NAME_IN_URL, NAME_DZEN, NAME_YANDEX

class TestRedirect:
    @allure.title('''Проверка редиректов при клике на логотипы в сервисе заказа''')
    @allure.title('''Тест проверяет редирект на главную страницу сервиса''')
    def test_logo_scooter_redirects_home(self, driver):
        page = MainPage(driver)
        page.open_main()
        page.click_logo_scooter()
        assert NAME_IN_URL in driver.current_url

    @allure.title('''Тест проверяет редирект на главную страницу дзена''')
    def test_logo_yandex_redirects_dzen(self, driver):
        page = MainPage(driver)
        page.open_main()
        start = len(driver.window_handles)
        page.click_logo_yandex()
        page.wait_new_tab_and_switch(start)
        page.wait_url_not("about:blank")
        cur = page.current_url().lower()
        assert (NAME_DZEN in cur) or (NAME_YANDEX in cur)