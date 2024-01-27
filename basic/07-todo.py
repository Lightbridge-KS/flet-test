import flet as ft

def main(page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    button = ft.ElevatedButton("Add", on_click=add_clicked) 
    page.add(
        ft.Row([new_task, button])
        )

ft.app(target=main)