import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        t.value = f"Textboxes values are:  {tb1.value=}"
        page.update()
        
    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "Enter":
            print("Enter")
            button_clicked(e)

    t = ft.Text()
    tb1 = ft.TextField(label="Standard")
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.on_keyboard_event = on_keyboard
    page.add(tb1, t, b)

ft.app(target=main)