import flet as ft

def main(page: ft.Page):
    rr = ft.ResponsiveRow([
        ft.Column(col=6, controls=[ft.Text("Column 1")]),
        ft.Column(col=6, controls=[ft.Text("Column 2")])
    ])
    
    page.add(rr)

ft.app(target=main)