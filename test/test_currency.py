from page_objects.elements.CurrencyElement import CurrencyElement


def test_currency_choise(browser):
    browser.get(browser.base_url)
    CurrencyElement(browser).change_currensy()
