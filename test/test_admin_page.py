from page_objects.AdminPage import AdminPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_data.users import get_admin
from test_data.products import get_product


def test_admin_page(browser):
    browser.get(browser.base_url + '/admin')
    AdminPage(browser).click_to_elements()


def test_add_new_product(browser):
    browser.get(browser.base_url + '/admin')
    AdminPage(browser).admin_login(*get_admin()) \
        .go_to_products() \
        .add_card(*get_product())


def test_delete_product(browser):
    browser.get(browser.base_url + '/admin')
    AdminPage(browser).admin_login(*get_admin()) \
        .go_to_products() \
        .delete_card()
    alert = WebDriverWait(browser, 2).until(EC.alert_is_present())
    alert.accept()
