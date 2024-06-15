from reactpy import component, html
@component
def THead(titles: list):
    return html._(
            html.thead(
                {
                "className":"sticky-top",
            },
            [html.th(key) for key in titles],
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
    
@component
def simple_table(titles,data):
    return html.table(
                {
                "className":"table table-striped w-100",
            },
            THead(titles),
            [TRow(fila) for fila in data]
        )