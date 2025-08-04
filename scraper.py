from playwright.sync_api import sync_playwright
import time

def fetch_case_data(case_type, case_number, filing_year):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://dhcmisc.nic.in/pcase/guiCaseWise.php")

        # Fill in form fields
        page.select_option("select[name='CT']", label=case_type)
        page.fill("input[name='CN']", case_number)
        page.fill("input[name='CY']", filing_year)

        # Wait for user to solve CAPTCHA manually
        print("🔐 Please solve the CAPTCHA in the browser...")
        time.sleep(30)  # or smarter wait as shown earlier

        # Submit the form
        page.click("input[type='submit']")

        # Wait for results to load
        page.wait_for_timeout(5000)

        # Get page content
        html = page.content()

        # Example data extraction (replace with actual selectors)
        data = {
            "parties": page.locator("selector-for-party-name").text_content(),
            "filing_date": page.locator("selector-for-filing-date").text_content(),
            "next_hearing": page.locator("selector-for-next-hearing").text_content(),
            "latest_order_link": "https://delhihighcourt.nic.in"  # placeholder
        }

        browser.close()
        return data, html
