from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page import COOKIE_BTN

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver,self.timeout)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def get_text(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text

    def scroll_to(self, locator):
        el = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)

    def accept_cookies(self):
        self.wait.until(EC.element_to_be_clickable(COOKIE_BTN))
        self.driver.find_element(*COOKIE_BTN).click()