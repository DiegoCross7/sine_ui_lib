def enviar_respuesta(page, texto):
    caja = page.locator("div[contenteditable='true']")
    caja.click()
    caja.type(texto)
    caja.press("Enter")
