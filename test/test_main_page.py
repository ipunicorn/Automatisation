from page_objects.MainPage import MainPage


def test_main_page(browser):
    browser.get(browser.base_url)
    MainPage(browser).click_to_elements()
