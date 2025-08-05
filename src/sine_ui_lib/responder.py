def enviar_respuesta(page, texto: str):
    caja = page.query_selector("div._2_1wd.copyable-text.selectable-text")
    caja.fill(texto)
    caja.press("Enter")
