import flet as ft

def main(page: ft.Page):
    # add/update controls on Page
    text_output = ft.Text("")
    
    storage_ls = []
    def save_clicked(e):
        storage_ls.append({"role": dropdown.value, "message": tb1.value})
        page.client_storage.set("storage", storage_ls)
        tb1.value = ""
        page.update()
        
    def show_clicked(e):
        storage = page.client_storage.get("storage")
        text_output.value = storage
        page.update()
    
    dropdown = ft.Dropdown(options=[ft.dropdown.Option("System"), 
                                    ft.dropdown.Option("User")])
    tb1 = ft.TextField(label="Input")
    btn_save = ft.ElevatedButton(text="Save", on_click=save_clicked)
    btn_show = ft.ElevatedButton(text="Show", on_click=show_clicked)
    
    page.add(dropdown, tb1, btn_save, btn_show, text_output)
    

ft.app(target=main)