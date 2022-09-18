from page_objects.ProductCardPage import ProductCardPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_card_page(browser):
    browser.get(browser.base_url + '/smartphone/htc-touch-hd')
    ProductCardPage(browser).click_to_elements()