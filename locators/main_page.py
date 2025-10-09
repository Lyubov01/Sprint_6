from selenium.webdriver.common.by import By
from urls import BASE_URL

COOKIE_BTN = (By.XPATH, "//button[normalize-space()='да все привыкли']")

class MainPageLocators: 
    URL = BASE_URL
    FAQ_BLOCK = (By.CLASS_NAME, "Home_FourPart__1uthg")
    QUESTIONS = (By.ID, "accordion__heading-{}")
    ANSWERS   = (By.ID, "accordion__panel-{}")

    ORDER_BUTTON_UP   = (By.XPATH, "(//button[@class='Button_Button__ra12g'])")
    ORDER_BUTTON_DOWN  = (By.CSS_SELECTOR, ".Button_Middle__1CSJM")

    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
    LOGO_YANDEX  = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")
