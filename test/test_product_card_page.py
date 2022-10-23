from page_objects.ProductCardPage import ProductCardPage


def test_product_card_page(browser):
    browser.get(browser.base_url + '/smartphone/htc-touch-hd')
    ProductCardPage(browser).click_to_elements()
