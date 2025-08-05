from playwright.sync_api import sync_playwright

def login_qr():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://web.whatsapp.com")
    print("Escanea el QR y presiona ENTER para continuar...")
    input()
    return page
