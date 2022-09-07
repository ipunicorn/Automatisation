from selenium.webdriver.common.by import By


class SignUpPage:
    FIRST_NAME_INPUT = (By.ID, 'input-firstname')
    LAST_NAME_INPUT = (By.ID, 'input-lastname')
    EMAIL_INPUT = (By.ID, 'input-email')
    RIGHT_MENU = (By.ID, 'column-right')
    CONTINUE_BUTTON = (By.XPATH, "//*[@id='content']")

