import pytest
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="browser for tests")
    parser.addoption("--base_url", default="http://127.0.0.1:4444/wd/hub", help="base url for tests")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--videos", action="store_true")
    parser.addoption("--bv")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    executor = request.config.getoption("--executor")
    log_level = request.config.getoption("--log_level")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    mobile = request.config.getoption("--mobile")

    class MyListener(AbstractEventListener):
        logger = logging.getLogger(request.node.name)
        logger.setLevel(logging.INFO)
        ch = logging.FileHandler(filename=f"logs/{request.node.name}.log")
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(logging.Formatter('%(asctime)s %(name)s:%(levelname)s %(message)s'))
        logger.addHandler(ch)

        def before_navigate_to(self, url, driver):
            self.logger.info(f"I'm navigating to {url} and {browser_name}")

        def after_navigate_to(self, url, driver):
            self.logger.info(f"I'm on {url}")

        def before_navigate_back(self, driver):
            self.logger.info(f"I'm navigating back")

        def after_navigate_back(self, driver):
            self.logger.info(f"I'm back!")

        def before_find(self, by, value, driver):
            self.logger.info(f"I'm looking for '{value}' with '{by}'")

        def after_find(self, by, value, driver):
            self.logger.info(f"I've found '{value}' with '{by}'")

        def before_click(self, element, driver):
            self.logger.info(f"I'm clicking {element}")

        def after_click(self, element, driver):
            self.logger.info(f"I've clicked {element}")

        def before_execute_script(self, script, driver):
            self.logger.info(f"I'm executing '{script}'")

        def after_execute_script(self, script, driver):
            self.logger.info(f"I've executed '{script}'")

        def before_quit(self, driver):
            self.logger.info(f"I'm getting ready to terminate {driver}")

        def after_quit(self, driver):
            self.logger.info(f"Driver Quit")

        def on_exception(self, exception, driver):
            self.logger.error(f'Oooops i got: {exception}')
            driver.save_screenshot(f'logs/{driver.session_id}.png')

    executor_url = f"http://{executor}:4444/wd/hub"

    caps = {
        "browserName": browser_name,
        "browserVersion": version,
        "screenResolution": "1280x720",
        "name": "Mikhail",
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": videos,
            "enableLog": logs
        },
        'acceptSslCerts': True,
        'acceptInsecureCerts': True,
        'timeZone': 'Europe/Moscow',
        'goog:chromeOptions': {}
    }

    options = Options()

    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=caps,
        options=options
    )

#if browser_name == "safari":
    #    driver = webdriver.Safari()

    driver = EventFiringWebDriver(driver, MyListener())
    driver.test_name = request.node.name
    driver.log_level = log_level
    driver.base_url = base_url
    driver.maximize_window()

    yield driver

    driver.close()
