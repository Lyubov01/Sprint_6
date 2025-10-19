from locators.order_page import OrderPageLocators as L
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import allure


class OrderPage(BasePage):
    
    @allure.step("Шаг 1: заполнить данные заказа (имя, фамилия, адрес, телефон)")
    def step1(self, name, surname, address, phone):
        self.type(L.INPUT_NAME, name)
        self.type(L.INPUT_SURNAME, surname)
        self.type(L.INPUT_ADDRESS, address)

        self.click(L.INPUT_METRO)
        self.find(L.INPUT_METRO).send_keys("м")
        self.wait_clickable(L.METRO_FIRST)
        self.click(L.METRO_FIRST)

        self.type(L.INPUT_PHONE, phone)
        self.click(L.NEXT_BUTTON)

        try:
            self.wait_visible(L.ORDER_HEADER_STEP2)
        except TimeoutException as exc:
            raise AssertionError("Не открылся шаг 2. Проверь выбор метро и валидацию.") from exc

    @allure.step("Шаг 2: выбрать дату, цвет и оформить заказ")
    def step2 (self, date, color, comment):
        self.type(L.DELIVERY_DATE, date)
        self.find(L.DELIVERY_DATE).send_keys(Keys.ENTER)

        self.click(L.RENT_DAYS)
        self.wait_clickable(L.RENT_OPTION_2DAYS)
        self.click(L.RENT_OPTION_2DAYS)

        if color == 'black':
            self.click(L.COLOR_BLACK)
        else:
            self.click(L.COLOR_GREY)

        self.type(L.COMMENT_FOR_DELIVER, comment)

        self.wait_clickable(L.ORDER_BUTTON)
        self.click(L.ORDER_BUTTON)

        self.wait_visible(L.PRE_CONFIRM_ORDER)
        self.click(L.YES_BUTTON)

        self.wait_visible(L.SUCCESSFUL_ORDER)

    @allure.step("Проверка: заказ успешно оформлен")
    def wait_success(self):
        return self.get_text(L.SUCCESSFUL_ORDER)