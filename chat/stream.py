import time
import flet as ft

def hello_generator():
    word = "HELLO"
    for letter in word:
        yield letter
        time.sleep(0.5)

def main(page: ft.Page):
    chat = ft.Row()

    def button_click(e):
        # Create a new generator instance every time the button is clicked
        hello_gen = hello_generator()
        for letter in hello_gen:
            chat.controls.append(
               ft.Container(ft.Text(letter), bgcolor=ft.colors.BLUE_GREY_200)
            )
            page.update()

    page.add(
        chat,
        ft.Row(controls=[ft.ElevatedButton("Gen", on_click=button_click)]),
    )


ft.app(target=main)