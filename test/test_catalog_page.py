from page_objects.CatalogPage import CatalogPage


def test_catalog_page(browser):
    browser.get(browser.base_url + '/smartphone')
    CatalogPage(browser).click_to_elements()
