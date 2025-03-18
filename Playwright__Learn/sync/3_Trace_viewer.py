# playwright codegen wikipedia.org
from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://www.wikipedia.org/")
    context.tracing.start(snapshots=True, screenshots=True, sources=True)
    page.get_by_role("navigation", name="Top languages").click()
    page.get_by_role("searchbox", name="Search Wikipedia").click()
    page.get_by_role("searchbox", name="Search Wikipedia").fill("ps5")
    page.get_by_role("link", name="PlayStation 5 Sony's fifth").click()
    page.get_by_role("link", name="Form factor", exact=True).click()

    # ---------------------
    # playwright show-trace trace.zip
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
