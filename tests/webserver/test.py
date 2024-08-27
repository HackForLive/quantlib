from pathlib import Path
from playwright.sync_api import sync_playwright, Playwright

script_path = Path(__file__).parent
output_path = Path.joinpath(script_path, 'example.png')

def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:9999")
    page.screenshot(path=output_path)
    # other actions...
    browser.close()

with sync_playwright() as playwright:
    run(playwright)