from selenium.webdriver.common.by import By


class ProductCardPage:
    BREADCRUMB = (By.CSS_SELECTOR, '.breadcrumb')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#product #button-cart')
    RATING_BLOCK = (By.XPATH, "//*[@class='rating']")
    DESCRIPTION_TAB = (By.XPATH, "//*[@data-toggle='tab']")
    REVIEW_TAB = (By.XPATH, "//*[@data-toggle='tab']")
