"""Genera las capturas del portafolio para la documentación del Módulo 8.

Uso:
    python tools/capture_portfolio.py

Levanta un servidor estático en el puerto 8099, abre el sitio con Chrome y guarda
las imágenes en docs/screenshots/.
"""

import http.server
import os
import socketserver
import threading

from playwright.sync_api import sync_playwright

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "docs", "screenshots")
PUERTO = 8099
BASE = f"http://127.0.0.1:{PUERTO}"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=RAIZ, **kwargs)

    def log_message(self, *args):  # silencio
        pass


def capturar():
    os.makedirs(SALIDA, exist_ok=True)
    servidor = socketserver.TCPServer(("127.0.0.1", PUERTO), Handler)
    hilo = threading.Thread(target=servidor.serve_forever, daemon=True)
    hilo.start()

    try:
        with sync_playwright() as p:
            navegador = p.chromium.launch(channel="chrome", headless=True)
            contexto = navegador.new_context(
                viewport={"width": 1440, "height": 900}, device_scale_factor=1
            )
            pagina = contexto.new_page()
            pagina.goto(BASE, wait_until="networkidle")
            pagina.wait_for_timeout(1200)

            def shot(nombre, selector=None, full=False):
                if selector:
                    pagina.eval_on_selector(selector, "el => el.scrollIntoView({block:'start'})")
                    pagina.wait_for_timeout(900)
                pagina.screenshot(path=os.path.join(SALIDA, nombre), full_page=full)
                print("capturado:", nombre)

            shot("01_hero.png")
            shot("02_sobre_mi.png", "#sobre-mi")
            shot("03_habilidades.png", "#habilidades")
            shot("04_proyectos.png", "#proyectos")
            shot("05_caso_estudio.png", "#caso-de-estudio")
            shot("06_empresa.png", "#empresa")
            shot("07_foda.png", "#foda")
            shot("08_contacto.png", "#contacto")

            # Vista móvil del hero para verificar el diseño responsivo.
            movil = navegador.new_context(
                viewport={"width": 390, "height": 844}, device_scale_factor=2
            )
            pm = movil.new_page()
            pm.goto(BASE, wait_until="networkidle")
            pm.wait_for_timeout(1000)
            pm.screenshot(path=os.path.join(SALIDA, "09_movil.png"))
            print("capturado: 09_movil.png")

            pagina.screenshot(path=os.path.join(SALIDA, "10_full_page.png"), full_page=True)
            print("capturado: 10_full_page.png")
            navegador.close()
    finally:
        servidor.shutdown()


if __name__ == "__main__":
    capturar()
    print("Listo ->", SALIDA)
