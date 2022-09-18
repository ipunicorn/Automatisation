from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    CART_BUTTON = (By.CSS_SELECTOR, '.btn.btn-inverse')
    FEATURED_STUFF = (By.CSS_SELECTOR, '.product-layout')
    SLIDESHOW = (By.CSS_SELECTOR, '.slideshow.swiper-viewport')
    MY_ACCOUNT = (By.XPATH, "//*[@title='My Account']")
    HEADER = (By.CSS_SELECTOR, '#logo .img-responsive')

    def click_to_elements(self):
        self.click(self.element(self.CART_BUTTON))
        self.click(self.element(self.SLIDESHOW))
        self.click(self.element(self.MY_ACCOUNT))
        self.click(self.element(self.HEADER))
        self.click(self.element(self.FEATURED_STUFF))
