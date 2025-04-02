from playwright.sync_api import Page
import pytest
from playwright.sync_api import BrowserType, BrowserContext

def test_title(page: Page):
    page.goto("https://www.saucedemo.com/")
    assert page.title() == 'Swag Labs'

# Test for skip browser
@pytest.mark.only_browser('chromium')
def test_youtube(page: Page):
    page.goto('https://youtube.com')
    assert page.title() == 'YouTube'

# Test for persistent context
def test_login_and_save_session(persistent_page: Page):
    persistent_page.goto("https://www.saucedemo.com/")
    persistent_page.fill('#user-name', 'standard_user')
    persistent_page.fill('#password', 'secret_sauce')
    persistent_page.click('#login-button')

    assert persistent_page.url == "https://www.saucedemo.com/inventory.html"

# test_after_login.py
def test_reuse_saved_session(persistent_page: Page):
    persistent_page.goto("https://www.saucedemo.com/inventory.html")
    assert persistent_page.title() == 'Swag Labs'
    assert persistent_page.url == "https://www.saucedemo.com/inventory.html"
