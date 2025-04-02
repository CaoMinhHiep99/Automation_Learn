import unittest
import pytest
from playwright.sync_api import Page


class MyTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup_page(self, page: Page):
        self.page = page

    def test_login_and_save_session(self):
        self.page.goto("https://www.saucedemo.com/")
        self.page.fill('#user-name', 'standard_user')
        self.page.fill('#password', 'secret_sauce')
        self.page.click('#login-button')
        assert self.page.url == "https://www.saucedemo.com/inventory.html"
