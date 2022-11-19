import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class SignUpPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, 'input-firstname')
    LAST_NAME_INPUT = (By.ID, 'input-lastname')
    EMAIL_INPUT = (By.ID, 'input-email')
    TELEPHONE = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, 'input-password')
    PASSWORD_CONFIRM = (By.ID, 'input-confirm')
    RIGHT_MENU = (By.ID, 'column-right')
    CONTINUE_BUTTON = (By.XPATH, "//*[@id='content']")
    MY_ACCOUNT = (By.XPATH, "//*[@title='My Account']")
    REGISTER_LINK = (By.LINK_TEXT, 'Register')

    def sign_up(self, firstname, lastname, email, telephone, password, passwordconfirm):
        self._input(self.element(self.FIRST_NAME_INPUT), firstname)
        self._input(self.element(self.LAST_NAME_INPUT), lastname)
        self._input(self.element(self.EMAIL_INPUT), email)
        self._input(self.element(self.TELEPHONE), telephone)
        self._input(self.element(self.PASSWORD), password)
        self._input(self.element(self.PASSWORD_CONFIRM), passwordconfirm)
        self.click(self.element(self.CONTINUE_BUTTON))
        return self

    @allure.step("Переход на страницу регистрации")
    def go_to_sign_up(self):
        self.click(self.element(self.MY_ACCOUNT))
        self.click(self.element(self.REGISTER_LINK))
        return self

    @allure.step("Клики по элементам")
    def click_to_elements(self):
        self.click(self.element(self.FIRST_NAME_INPUT))
        self.click(self.element(self.LAST_NAME_INPUT))
        self.click(self.element(self.EMAIL_INPUT))
        self.click(self.element(self.RIGHT_MENU))
        self.click(self.element(self.CONTINUE_BUTTON))
