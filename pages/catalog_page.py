from selenium.webdriver.common.by import By


class CatalogPage:
    BREADCRUMB = (By.CSS_SELECTOR, '.breadcrumb')
    LEFT_MENU = (By.ID, 'column-left')
    SORT_BY = (By.CSS_SELECTOR, '.form-control')
    PRODUCTS = (By.CSS_SELECTOR, '.product-layout')
    PAGES_COUNTER = (By.CSS_SELECTOR, '.col-sm-6.text-right')
