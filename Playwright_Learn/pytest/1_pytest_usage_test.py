from playwright.sync_api import Page
import pytest


def test_title(page: Page):
    page.goto("https://www.saucedemo.com/")
    assert page.title() == 'Swag Labs'

@pytest.mark.only_browser('chromium')
def test_youtube(page: Page):
    page.goto('https://youtube.com')
    assert page.title() == 'YouTube'