import asyncio
from playwright.async_api import async_playwright

async def open_browsers():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()

        page1 = await context.new_page()
        await page1.goto("http://playwright.dev")

        page2 = await context.new_page()
        await page2.goto("http://google.com")

        # Keep the browser open for a while to see the pages
        await asyncio.sleep(10)
        await browser.close()

asyncio.run(open_browsers())