import time
import flet as ft
from typing import Generator

def hello_generator() -> Generator[str, None, None]:
    word = "HELLO"
    for letter in word:
        yield letter
        time.sleep(0.5)

def main(page: ft.Page):
    # Create a container that will hold all letters
    text_container = ft.Container(
        content=ft.Text("", size=24),  # Initially empty
        bgcolor=ft.colors.BLUE_GREY_200
    )

    def button_click(e):
        # Create a new generator instance every time the button is clicked
        hello_gen = hello_generator()
        for letter in hello_gen:
            # Append each letter to the container's content
            text_container.content.value += letter
            page.update()  # Update the page to reflect the changes

    # Add the text container and button to the page
    page.add(
        ft.Row([text_container]),
        ft.Row([ft.ElevatedButton("Gen", on_click=button_click)]),
    )

ft.app(target=main)
