# See more example at: https://flet.dev/docs/controls/textfield

import flet as ft
from flet import Container, Column

class MyTextFields(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.t = ft.Text()
        self.tb1 = ft.TextField(label="Standard")
        self.tb2 = ft.TextField(label="Disabled", disabled=True, value="First name")
        self.tb3 = ft.TextField(label="Read-only", read_only=True, value="Last name")
        self.tb4 = ft.TextField(label="With placeholder", hint_text="Please enter text here")
        self.tb5 = ft.TextField(label="With an icon", icon=ft.icons.EMOJI_EMOTIONS)
        self.b = ft.ElevatedButton(text="Submit", on_click=self.button_clicked)
   
    def button_clicked(self, e):
        self.t.value = f"Textboxes values are:  '{self.tb1.value}', '{self.tb2.value}', '{self.tb3.value}', '{self.tb4.value}', '{self.tb5.value}'. type of '{self.tb1.value}' =  {type(self.tb1.value)}"
        self.update()
        
    def build(self):
        return ft.Column([ self.t, self.tb1, self.tb2, self.tb3, self.tb4, self.tb5, self.b])
      
      
  
if __name__ == "__main__":
    def main(page: ft.Page):
        page.title = "MyTextFieldApp"
        app1 = MyTextFields()
        
        page.add(app1)
        
    ft.app(target=main)