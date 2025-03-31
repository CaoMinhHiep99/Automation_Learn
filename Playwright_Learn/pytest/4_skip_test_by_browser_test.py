from playwright.sync_api import Page
import pytest


@pytest.mark.only_browser('chromium')
def test_youtube_only_browser(page: Page):
    page.goto('https://youtube.com')
    assert page.title() == 'YouTube'

@pytest.mark.skip_browser('chromium')
def test_youtube(page: Page):
    page.goto('https://youtube.com')
    assert page.title() == 'YouTube'