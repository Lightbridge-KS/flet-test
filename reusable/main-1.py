import flet as ft
from module.mydropdown import MyDropDown

def main(page: ft.Page):
    # Create an instance of MyDropDown with desired options
    dropdown_component = MyDropDown(
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ]
    )

    # Add the MyDropDown component to the page
    page.add(dropdown_component)

ft.app(target=main)
