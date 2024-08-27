import asyncio
from pathlib import Path

from playwright.async_api import async_playwright, Playwright

script_path = Path(__file__).parent
output_path = Path.joinpath(script_path, 'example.png')

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch()
    page = await browser.new_page()
    
    await page.goto("http://localhost:9999")
    await page.screenshot(path=output_path)
    # other actions...
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())