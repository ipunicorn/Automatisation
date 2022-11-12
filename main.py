if __name__ == '__main__':
    print("Hello, World!")


import pytest
import logging

from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="browser for tests"
    )
    parser.addoption(
        "--base_url", default="http://localhost/", help="base url for tests"
    )
    parser.addoption(
        "--log_level", action="store", default="DEBUG"
    )


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    log_level = request.config.getoption("--log_level")

    class MyListener(AbstractEventListener):
        logger = logging.getLogger(request.node.name)
        logger.setLevel(logging.INFO)
        ch = logging.FileHandler(filename=f"logs/{request.node.name}.log")
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(logging.Formatter('%(asctime)s %(name)s:%(levelname)s %(message)s'))
        logger.addHandler(ch)

        def before_navigate_to(self, url, _browser):
            self.logger.info(f"I'm navigating to {url} and {_browser.title}")

        def after_navigate_to(self, url, _browser):
            self.logger.info(f"I'm on {url}")

        def before_navigate_back(self, _browser):
            self.logger.info(f"I'm navigating back")

        def after_navigate_back(self, _browser):
            self.logger.info(f"I'm back!")

        def before_find(self, by, value, _browser):
            self.logger.info(f"I'm looking for '{value}' with '{by}'")

        def after_find(self, by, value, _browser):
            self.logger.info(f"I've found '{value}' with '{by}'")

        def before_click(self, element, _browser):
            self.logger.info(f"I'm clicking {element}")

        def after_click(self, element, driver):
            self.logger.info(f"I've clicked {element}")

        def before_execute_script(self, script, _browser):
            self.logger.info(f"I'm executing '{script}'")

        def after_execute_script(self, script, _browser):
            self.logger.info(f"I've executed '{script}'")

        def before_quit(self, _browser):
            self.logger.info(f"I'm getting ready to terminate {_browser}")

        def after_quit(self, _browser):
            self.logger.info(f"Driver Quit")

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

    _browser = EventFiringWebDriver(_browser, MyListener())
    _browser.test_name = request.node.name
    _browser.log_level = log_level
    _browser.base_url = base_url
    _browser.maximize_window()

    yield _browser

    _browser.close()
