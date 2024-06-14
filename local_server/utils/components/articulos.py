from reactpy import component, html

@component
def THead(datos: dict):
    if datos:  # Verifica si 'datos' no está vacío
        cols = datos[0].keys()
    else:
        cols = []


    return html._(
            html.thead(
                {
                "className":"sticky-top",
            },
            [html.th(key) for key in cols],
            )
        )

@component
def TRow(datos: dict):
    fila = datos.values()

    return html._(
            html.tr(
            [html.td(value) for value in fila],
            )
        )
