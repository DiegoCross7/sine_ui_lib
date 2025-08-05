def leer_mensaje(page, selector: str) -> str:
    elemento = page.query_selector(selector)
    return elemento.inner_text().strip() if elemento else ""
