import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage 
from data import DATA_1_FOR_ORDER, DATA_2_FOR_ORDER, ENTRY_BUTTON, ORDER_DONE

class TestOrder:
    @allure.title('''
    Проверка создания заказа через верхнюю и нижнюю кнопки "Заказать":
    1. Заполнение формы заказа тестовыми данными, имеются 2 набора данных
    2. Проверка успешного оформления заказа по наличию текста подтверждения
    3. Проверка наличия окна подтверждения заказа''')   
    @pytest.mark.parametrize("data", [DATA_1_FOR_ORDER, DATA_2_FOR_ORDER])
    @pytest.mark.parametrize("entry", ENTRY_BUTTON)
    def test_order_positive(self,driver, data, entry):
        main = MainPage(driver)
        order = OrderPage(driver)
        main.open_main()
        main.click_order(entry)
        order.step1(data["name"], data["surname"], data["address"], data["phone"])
        order.step2(data["day"], data["color"], data["comment"])
        assert ORDER_DONE in order.wait_success()
