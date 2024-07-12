import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        t.value = f"Textboxes values are:  {tb1.value=}"
        page.update()


    t = ft.Text()
    tb1 = ft.TextField(label="Standard", on_submit = button_clicked) # Key
    
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    

    page.add(tb1, t, b)

ft.app(target=main)