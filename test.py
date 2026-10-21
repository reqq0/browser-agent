import asyncio
from playwright.async_api import async_playwright
entry=str(input("Enter what you want to search: "))
async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False,slow_mo=1000)
        page= await browser.new_page()
        await page.goto("https://www.duckduckgo.com")
        search = page.get_by_placeholder("Search privately")
        await search.fill(entry)
        await search.press("Enter")
        await page.wait_for_load_state('networkidle')
        await page.screenshot(path='screenshot.png',full_page=True,type="png")
asyncio.run(main())    

