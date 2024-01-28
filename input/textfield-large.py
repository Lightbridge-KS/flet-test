import flet as ft

def main(page: ft.Page):
    # add/update controls on Page
    tb1 = ft.TextField(label="MultiLine", value="X\n"*5, multiline=True)
    page.add(tb1)

ft.app(target=main)