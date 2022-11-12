import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class CatalogPage(BasePage):
    BREADCRUMB = (By.CSS_SELECTOR, '.breadcrumb')
    LEFT_MENU = (By.ID, 'column-left')
    SORT_BY = (By.CSS_SELECTOR, '.form-control')
    PRODUCTS = (By.CSS_SELECTOR, '.product-layout')
    PAGES_COUNTER = (By.CSS_SELECTOR, '.col-sm-6.text-right')

    @allure.step("Клики по элементам")
    def click_to_elements(self):
        self.click(self.element(self.BREADCRUMB))
        self.click(self.element(self.LEFT_MENU))
        self.click(self.element(self.SORT_BY))
        self.click(self.element(self.PAGES_COUNTER))
        self.click(self.element(self.PRODUCTS))
