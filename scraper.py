from playwright.sync_api import sync_playwright
import time

def fetch_case_data(case_type, case_number, filing_year):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True later
        page = browser.new_page()
        page.goto("https://delhihighcourt.nic.in/case.asp")

        # Fill in the form
        page.select_option("select[name='CT']",
                           label=case_type)  # e.g., 'W.P. (C)' or 'C.M.(M)'
        page.fill("input[name='CN']", case_number)
        page.fill("input[name='CY']", filing_year)

        # ❗ Wait for user to solve CAPTCHA manually
        print("Please solve CAPTCHA in the browser. Waiting...")
        time.sleep(30)

        # Submit the form
        page.click("input[type='submit']")

        # Wait for results
        page.wait_for_timeout(5000)

        html = page.content()

        # Extract data using Playwright or BeautifulSoup
        # For demo, we return mock data
        data = {
            "parties": "N/A",
            "filing_date": "N/A",
            "next_hearing": "N/A",
            "latest_order_link": "https://delhihighcourt.nic.in"  # placeholder
        }

        browser.close()
        return data, html
