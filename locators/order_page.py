from selenium.webdriver.common.by import By

class OrderPageLocators:
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//*[contains(@class,'select-search__value')]")
    METRO_FIRST = (By.XPATH,"(//button[contains(@class,'select-search__option') "
    "and not(contains(@class,'is-hidden'))])[1]")
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[.='Далее']")

    DELIVERY_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DAYS = (By.XPATH, "//span[@class='Dropdown-arrow']")
    RENT_OPTION_2DAYS = (By.XPATH, "//div[@class='Dropdown-menu']//div[text()='двое суток']")
    ORDER_HEADER_STEP2 = (By.XPATH, "//*[contains(@class,'Order_Header') and contains(.,'Про аренду')]")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FOR_DELIVER = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]')
    PRE_CONFIRM_ORDER = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESSFUL_ORDER = (By.XPATH, "//div[contains(text(),'Заказ оформлен')]")
