from typing import Dict
import pytest
from playwright.sync_api import sync_playwright, Playwright
from playwright.sync_api import BrowserType, BrowserContext

# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#         **browser_context_args,
#         "viewport": {
#             "width": 1920,
#             "height": 1080,
#         }}

# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args, playwright: Playwright):
#     iphone_12 = playwright.devices['iPhone 12']
#     return {
#         **browser_context_args,
#         **iphone_12,
#     }

@pytest.fixture(scope="session")
def persistent_context(
    browser_type: BrowserType,
    browser_type_launch_args: Dict,
    browser_context_args: Dict,
) -> BrowserContext: # type: ignore
    context = browser_type.launch_persistent_context(
        "./foobar",
        **{
            **browser_type_launch_args,
            **browser_context_args,
        }
    )
    yield context
    context.close()

@pytest.fixture
def persistent_page(persistent_context: BrowserContext):
    page = persistent_context.new_page()
    yield page
    page.close()
