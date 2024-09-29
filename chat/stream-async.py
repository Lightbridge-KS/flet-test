# Not Work Yet

import time
import asyncio
import flet as ft

# Asynchronous generator function
async def hello_generator():
    word = "HELLO"
    for letter in word:
        print("-", letter, "-")
        yield letter
        await asyncio.sleep(0.5)  # Use await to sleep asynchronously

def main(page: ft.Page):
    chat = ft.Column()

    async def button_click(e):
        # Create a new generator instance every time the button is clicked
        hello_gen = hello_generator()
        async for letter in hello_gen:  # Asynchronous iteration over the generator
            chat.controls.append(ft.Text(letter))
            page.update()

    # Create an async button click handler to execute the asynchronous button_click function
    page.add(
        chat,
        ft.Row(controls=[ft.ElevatedButton("Gen", on_click=lambda e: asyncio.create_task(button_click(e)))]),
    )

ft.app(target=main)
