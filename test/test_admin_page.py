from pages.admin_page import AdminPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_admin_page(browser):
    browser.get(browser.base_url + '/admin')
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(AdminPage.USERNAME_INPUT))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(AdminPage.LOGIN_BUTTON))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(AdminPage.LOGIN_BUTTON))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(AdminPage.FORGOT_PASSWORD))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(AdminPage.OPENCART_LINK))

