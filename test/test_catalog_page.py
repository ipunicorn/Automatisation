from page_objects.CatalogPage import CatalogPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_catalog_page(browser):
    browser.get(browser.base_url + '/smartphone')
    CatalogPage(browser).click_to_elements()
