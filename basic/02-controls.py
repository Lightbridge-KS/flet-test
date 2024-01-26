import flet as ft

def main(page: ft.Page):
    # To display control on a page add it to controls list of a Page
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    # call page.update() to send page changes to a browser or desktop client:
    page.update()

ft.app(target=main)