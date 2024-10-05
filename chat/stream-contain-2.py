import time
import flet as ft
from typing import Generator

# Generator function that yields each letter from "HELLO" with a delay
def hello_generator() -> Generator[str, None, None]:
    word = "HELLO"
    for letter in word:
        yield letter
        time.sleep(0.5)

def main(page: ft.Page):
    # Container to hold multiple Text elements, each displaying "HELLO"
    text_column = ft.Column()

    def button_click(e):
        # Create a new generator instance every time the button is clicked
        hello_gen = hello_generator()

        # Create a new Text object to hold the generated "HELLO" letters
        # new_text = ft.Text("", size=24)
        new_container = ft.Container(
            content=ft.Text("", size=24),  # Initially empty
            bgcolor=ft.colors.BLACK87
        )
        text_column.controls.append(new_container)

        # Iterate through the generator and update the new Text object
        for letter in hello_gen:
            new_container.content.value += letter
            page.update()  # Update the page to reflect the changes in real-time

    # Add the text column and button to the page
    page.add(
        text_column,
        ft.Row([ft.ElevatedButton("Gen", on_click=button_click)]),
    )

ft.app(target=main)
