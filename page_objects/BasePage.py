from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def _input(self, element, value):
        self.click(element)
        element.clear()
        element.send_keys(value)

    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    def click(self, element):
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()
