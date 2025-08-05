def leer_mensaje(page):
    # Selector por defecto para el último mensaje recibido
    selector = "div.message-in span[dir='ltr']"
    mensajes = page.locator(selector).all_inner_texts()
    if mensajes:
        return mensajes[-1].strip()
    return None
