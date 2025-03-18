# playwright codegen wikipedia.org
from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://www.wikipedia.org/")
    page.get_by_role("navigation", name="Top languages").click()
    page.get_by_role("searchbox", name="Search Wikipedia").click()
    page.get_by_role("searchbox", name="Search Wikipedia").fill("ps5")
    page.get_by_role("link", name="PlayStation 5 Sony's fifth").click()
    page.get_by_role("link", name="Form factor", exact=True).click()

    # ---------------------
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
