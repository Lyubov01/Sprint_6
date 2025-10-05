from locators.main_page import MainPageLocators as L
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class MainPage(BasePage):
    def open_main(self):
        self.open(L.URL)
        self.accept_cookies()

    def _q(self, idx:int):
        return (L.QUESTIONS[0], L.QUESTIONS[1].format(idx))

    def _a(self, idx:int):
        return (L.ANSWERS[0], L.ANSWERS[1].format(idx))

    def scroll_to_faq(self):
        self.scroll_to(L.FAQ_BLOCK)

    def toggle_question(self, idx:int):
        loc = self._q(idx)
        self.scroll_to(loc)
        self.click(loc)

    def wait_answer_visible(self, idx:int):
        self.wait.until(EC.visibility_of_element_located(self._a(idx)))

    def answer_text(self, idx:int):
        return self.get_text(self._a(idx))

    def click_order(self, where):
        if where == "up":
            self.click(L.ORDER_BUTTON_UP)
        else:
            self.click(L.ORDER_BUTTON_DOWN)

    def click_logo_scooter(self):
        self.click(L.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click(L.LOGO_YANDEX)
