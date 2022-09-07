import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="browser for tests"
    )
    parser.addoption(
        "--base_url", default="http://localhost/", help="base url for tests"
    )


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")

    if browser_name == "chrome":
        _browser = webdriver.Chrome()
    elif browser_name == "safari":
        _browser = webdriver.Safari()
    elif browser_name == "firefox":
        _browser = webdriver.Firefox()
    elif browser_name == "opera":
        _browser = webdriver.Opera()
    else:
        raise ValueError(f"Browser {browser_name} is not supported.")

    _browser.base_url = base_url
    _browser.maximize_window()

    yield _browser

    _browser.close()
