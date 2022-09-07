from selenium.webdriver.common.by import By


class MainPage:
    CART_BUTTON = (By.CSS_SELECTOR, '.btn.btn-inverse')
    FEATURED_STUFF = (By.CSS_SELECTOR, '.product-layout')
    SLIDESHOW = (By.CSS_SELECTOR, '.slideshow.swiper-viewport')
    MY_ACCOUNT = (By.XPATH, "//*[@title='My Account']")
    HEADER = (By.CSS_SELECTOR, '#logo .img-responsive')
