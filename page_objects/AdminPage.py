from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.ID, 'input-password')
    LOGIN_BUTTON = (By.XPATH, "//*[@type='submit']")
    FORGOT_PASSWORD = (By.LINK_TEXT, 'Forgotten Password')
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    MENU_ITEM = (By.ID, 'menu')
    PRODUCTS_LIST_LINK = (By.LINK_TEXT, 'Products')
    CATALOG_ITEM = (By.ID, 'menu-catalog')
    ADD_NEW = (By.XPATH, "//*[@data-original-title='Add New']")
    PRODUCT_NAME = (By.XPATH, "//*[@name='product_description[1][name]']")
    META = (By.XPATH, "//*[@name='product_description[1][meta_title]']")
    MODEL = (By.XPATH, "//*[@name='model']")
    DATA_TAB = (By.LINK_TEXT, 'Data')
    SAVE_PRODUCT = (By.XPATH, "//*[@data-original-title='Save']")
    DELETE_PRODUCT = (By.XPATH, "//*[@data-original-title='Delete']")
    CHECKBOX_TO_DELETE = (By.XPATH, "//*[@name='selected[]']")

    def admin_login(self, username, password):
        self._input(self.element(self.USERNAME_INPUT), username)
        self._input(self.element(self.PASSWORD_INPUT), password)
        self.click(self.element(self.LOGIN_BUTTON))
        return self

    def go_to_products(self):
        self.click(self.element(self.CATALOG_ITEM))
        self.click(self.element(self.PRODUCTS_LIST_LINK))
        return self

    def add_card(self, productname, meta, model):
        self.click(self.element(self.ADD_NEW))
        self._input(self.element(self.PRODUCT_NAME), productname)
        self._input(self.element(self.META), meta)
        self.click(self.element(self.DATA_TAB))
        self._input(self.element(self.MODEL), model)
        self.click(self.element(self.SAVE_PRODUCT))
        return self

    def delete_card(self):
        self.click(self.element(self.CHECKBOX_TO_DELETE))
        self.click(self.element(self.DELETE_PRODUCT))

    def click_to_elements(self):
        self.click(self.element(self.USERNAME_INPUT))
        self.click(self.element(self.PASSWORD_INPUT))
        self.click(self.element(self.LOGIN_BUTTON))
        self.click(self.element(self.FORGOT_PASSWORD))
        self.click(self.element(self.OPENCART_LINK))
