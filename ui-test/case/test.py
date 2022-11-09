import pytest
import uuid

from selenium import webdriver
from selenium.common.exceptions import TimeoutException


class TestClass:

    @pytest.yield_fixture(autouse=True)
    def init_browser(self):
        self.browser = webdriver.Remote(
            desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
            command_executor='http://my-selenium:4444/wd/hub'
        )
        yield  # everything after 'yield' is executed on tear-down
        self.browser.quit()

    @pytest.mark.parametrize('data', [1, 2, 3, 4])
    def test_buybuttons(self, data):
        self.browser.get('http://example.com/' + data)
        assert '<noindex>' not in self.browser.page_source
