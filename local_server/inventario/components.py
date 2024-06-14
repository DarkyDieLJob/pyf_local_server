from reactpy import component, html

from utils.components.articulos import THead, TRow


@component
def hello_world(recipient: str, datos: dict):
    return html._(
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
        ),
        html.h1(f"Hello {recipient}!"),
        html.div(
            {
                "className":"overflow-auto h-100",
            },
            html.table(
                    {
                    "className":"table table-striped w-100",
                },
                THead(datos),
                [TRow(fila) for fila in datos]
            )
        )
    )