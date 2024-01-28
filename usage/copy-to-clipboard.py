import flet as ft
import pyperclip

def main(page: ft.Page):
    page.title = "Icon buttons"
    
    def copy_text(e):
        pyperclip.copy(tb.value)
    
    tb = ft.TextField(label="Text", value="Some Text")
    
    icon_copy = ft.IconButton(
                    icon=ft.icons.CONTENT_COPY,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="Copy content",
                    on_click=copy_text
                )
    
    page.add(
        ft.Row([tb, icon_copy])
    )


ft.app(target=main)