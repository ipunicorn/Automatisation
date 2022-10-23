from page_objects.SignUpPage import SignUpPage
from test_data.users import get_new_user


def test_sign_up_page(browser):
    browser.get(browser.base_url + '/index.php?route=account/register')
    SignUpPage(browser).click_to_elements()


def test_sign_up(browser):
    browser.get(browser.base_url)
    SignUpPage(browser).go_to_sign_up().sign_up(*get_new_user())
