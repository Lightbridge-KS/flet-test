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
    tb = ft.TextField(label="Standard", multiline=True, value="\n"*10)
    
    rr = ft.ResponsiveRow([
        ft.Column(col={"sm": 6}, controls=[dd, dd, ft.ResponsiveRow([dd, dd])]),
        ft.Column(col={"sm": 6}, controls=[tb]),
    ])
    page.add(rr)

ft.app(target=main)