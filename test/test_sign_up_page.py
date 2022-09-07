from pages.sign_up_page import SignUpPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_sign_up_page(browser):
    browser.get(browser.base_url + '/index.php?route=account/register')
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(SignUpPage.FIRST_NAME_INPUT))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(SignUpPage.LAST_NAME_INPUT))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(SignUpPage.EMAIL_INPUT))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(SignUpPage.RIGHT_MENU))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(SignUpPage.CONTINUE_BUTTON))
