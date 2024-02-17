import flet as ft

def main(page: ft.Page):
    # add/update controls on Page
    dd = ft.Dropdown(
        # expand=True,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ]
    )
    rr = ft.ResponsiveRow([
        ft.Column(col={"sm": 12}, controls=[dd]),
        ft.Column(col={"sm": 6}, controls=[dd]),
        ft.Column(col={"sm": 6}, controls=[dd])
    ])
    page.add(rr)

ft.app(target=main)