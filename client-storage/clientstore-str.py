import flet as ft

def main(page: ft.Page):
    # add/update controls on Page
    text_output = ft.Text("")
    
    def save_clicked(e):
        page.client_storage.set("key1", tb1.value)
        tb1.value = ""
        page.update()
    def show_clicked(e):
        key1 = page.client_storage.get("key1")
        text_output.value = key1
        page.update()
    
    tb1 = ft.TextField(label="Input")
    btn_save = ft.ElevatedButton(text="Save", on_click=save_clicked)
    btn_show = ft.ElevatedButton(text="Show", on_click=show_clicked)
    
    page.add(tb1, btn_save, btn_show, text_output)
    

ft.app(target=main)