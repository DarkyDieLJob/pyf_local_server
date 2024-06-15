from reactpy import component, html

from utils.components.html import encabezado, cuerpo
from utils.components.html_table import simple_table




@component
def listar_articulos(h2: str, datos: dict):
    elementos = [
        html.h2(f"Lista de {h2}!"),
        html.div(
            {
                "className":"overflow-auto h-100",
            },
            simple_table(datos[0].keys(), datos),
        )
        ]
    return html._(
        encabezado(),
        cuerpo(elementos)
        
    )