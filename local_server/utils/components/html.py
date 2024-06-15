from reactpy import component, html

@component
def encabezado():
    links = [
        html.link(
            {
                "href":"https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css",
                "rel":"stylesheet"
            }
        ),
        html.link(
            {
                "href":"https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css",
                "rel":"stylesheet"
            }
        )
    ]
    return html.header(links)

@component
def cuerpo(elementos):
    return html._(
        elementos,
    )

@component
def pie():
    return html.footer()