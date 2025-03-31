import pytest
from playwright.sync_api import sync_playwright, Playwright

# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#         **browser_context_args,
#         "viewport": {
#             "width": 1920,
#             "height": 1080,
#         }}

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright: Playwright):
    iphone_12 = playwright.devices['iPhone 12']
    return {
        **browser_context_args,
        **iphone_12,
    }