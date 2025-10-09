from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver,self.timeout)

    @allure.step('Открыть страницу сайта')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Выполнить поиск элемента с ожиданием')
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Ввод текста в поле')
    def type(self, locator, text):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)

    @allure.step("Найти элемент")
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Получить текст")
    def get_text(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text

    @allure.step("Прокрутить до нужного элемента")
    def scroll_to(self, locator):
        el = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)

    @allure.step("Принять cookies")
    def accept_cookies(self, locator):
        self.wait_clickable(locator).click()

    @allure.step('Дождаться появления элемента')
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Дождаться пока пока элемент станет кликабельным')
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step('Дождаться появление элемента')
    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))
    
    @allure.step("Ожидание открытия новой вкладки и переключение на неё")
    def wait_new_tab_and_switch(self, start_handles_count: int):
        self.wait.until(lambda d: len(d.window_handles) > start_handles_count)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ожидание изменения URL")
    def wait_url_not(self, privios_url: str):
        self.wait.until(lambda d: d.current_url != privios_url)   

    @allure.step("Получить текущий URL страницы")
    def current_url(self):
        return self.driver.current_url  