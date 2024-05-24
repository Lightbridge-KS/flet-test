# See more example at: https://flet.dev/docs/controls/textfield
from datetime import date
import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        t.value = f"Textboxes values are: {input_date.value}"
        page.update()

    t = ft.Text()
    input_date = ft.TextField(label="Date", value=date.today().strftime('%d/%m/%Y'))
    b = ft.ElevatedButton(text="Submit",  on_click=button_clicked)
    page.add(b, input_date, t)

ft.app(target=main)