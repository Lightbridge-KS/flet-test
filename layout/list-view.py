import flet as ft


def main(page: ft.Page):
    # add/update controls on Page
    dd = ft.Dropdown(
        # expand=True,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ]
    )
    
    lv = ft.ListView(controls=[dd, dd, dd, dd, dd, dd, dd, dd, dd, dd, dd], 
                     expand=1,  spacing=10, padding=20, auto_scroll=True) # spacing=10, padding=20
    
    page.add(lv)


ft.app(target=main)
