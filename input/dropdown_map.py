import flet as ft

lookup = ["Red", "Green", "Blue"]

def main(page: ft.Page):
    def button_clicked(e):
        t.value = f"Dropdown value is:  {dd.value}"
        page.update()

    t = ft.Text()
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    dd = ft.Dropdown(
        width=100,
        options=[ft.dropdown.Option(x) for x in lookup]
    )
    page.add(dd, b, t)

ft.app(target=main)