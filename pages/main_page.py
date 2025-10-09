from locators.main_page import MainPageLocators as L
from pages.base_page import BasePage
from locators.main_page import COOKIE_BTN
import allure

class MainPage(BasePage):
    
    @allure.step("Открыть главную страницу и принять cookies")
    def open_main(self):
        self.open(L.URL)
        self.accept_cookies(COOKIE_BTN)

    def _q(self, idx:int):
        return (L.QUESTIONS[0], L.QUESTIONS[1].format(idx))

    def _a(self, idx:int):
        return (L.ANSWERS[0], L.ANSWERS[1].format(idx))

    @allure.step("Прокрутить до блока FAQ")
    def scroll_to_faq(self):
        self.scroll_to(L.FAQ_BLOCK)

    @allure.step("Развернуть вопрос")
    def toggle_question(self, idx:int):
        loc = self._q(idx)
        self.scroll_to(loc)
        self.click(loc)

    @allure.step("Ожидать появления ответа для вопроса")
    def wait_answer_visible(self, idx:int):
        self.wait_visible(self._a(idx))

    @allure.step("Получить текст ответа для вопроса")
    def answer_text(self, idx:int):
        return self.get_text(self._a(idx))

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order(self, where):
        if where == "up":
            self.click(L.ORDER_BUTTON_UP)
        else:
            self.click(L.ORDER_BUTTON_DOWN)

    @allure.step("Клик по логотипу Scooter")
    def click_logo_scooter(self):
        self.click(L.LOGO_SCOOTER)

    @allure.step("Клик по логотипу Yandex")
    def click_logo_yandex(self):
        self.click(L.LOGO_YANDEX)
