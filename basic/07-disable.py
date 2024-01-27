import flet as ft

def main(page: ft.Page):
    first_name = ft.TextField()
    last_name = ft.TextField()
    age = ft.TextField()
    
    c = ft.Column(controls=[
    first_name,
    last_name
    ])
    c.disabled = True
    page.add(c)
    page.add(age)

ft.app(target=main)