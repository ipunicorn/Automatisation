from pages.catalog_page import CatalogPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_catalog_page(browser):
    browser.get(browser.base_url + '/smartphone')
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(CatalogPage.BREADCRUMB))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(CatalogPage.LEFT_MENU))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(CatalogPage.SORT_BY))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(CatalogPage.PAGES_COUNTER))
    WebDriverWait(browser, 2).until(EC.visibility_of_all_elements_located(CatalogPage.PRODUCTS))
