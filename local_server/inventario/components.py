from reactpy import component, html

@component
def hello_world(recipient: str):
    return html._(
        html.h1(f"Hello {recipient}!"),
        html.ul(
            html.li('item1'),
            html.li('item2')
        )
        )

