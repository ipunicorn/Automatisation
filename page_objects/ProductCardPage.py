import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class ProductCardPage(BasePage):
    BREADCRUMB = (By.CSS_SELECTOR, '.breadcrumb')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#product #button-cart')
    RATING_BLOCK = (By.XPATH, "//*[@class='rating']")
    DESCRIPTION_TAB = (By.XPATH, "//*[@data-toggle='tab']")
    REVIEW_TAB = (By.XPATH, "//*[@data-toggle='tab']")

    @allure.step("Клики по элементам")
    def click_to_elements(self):
        self.click(self.element(self.BREADCRUMB))
        self.click(self.element(self.RATING_BLOCK))
        self.click(self.element(self.DESCRIPTION_TAB))
        self.click(self.element(self.REVIEW_TAB))
        self.click(self.element(self.ADD_TO_CART_BUTTON))
