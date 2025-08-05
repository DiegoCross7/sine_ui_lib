from playwright.sync_api import sync_playwright

def login_qr():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://web.whatsapp.com")
    print("Escanea el código QR para iniciar sesión...")
    page.wait_for_selector("canvas[aria-label='Scan me!']", state="detached")
    print("✅ Sesión iniciada correctamente")
    return page
