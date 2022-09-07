from pages.product_card_page import ProductCardPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_card_page(browser):
    browser.get(browser.base_url + '/smartphone/htc-touch-hd')
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(ProductCardPage.BREADCRUMB))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(ProductCardPage.ADD_TO_CART_BUTTON))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(ProductCardPage.RATING_BLOCK))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(ProductCardPage.DESCRIPTION_TAB))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(ProductCardPage.REVIEW_TAB))
