import flet as ft
from flet import (
    Container,
    Column,
    Row,
    ElevatedButton,
    Page,
    UserControl,
)

class MyInput(UserControl):
    def __init__(self):
        super().__init__()
        self.t = ft.Text("Initial Text")
        self.tb1 = ft.TextField(label="Standard")
        self.button = ft.ElevatedButton("Show", on_click=self.button_clicked) 

    def build(self):
        return Container(
            content=Column(
                [self.t, self.tb1, self.button]
            )
        )
    def button_clicked(self, e):
        print(f"TextField = {self.tb1.value}")
        self.t.value = self.tb1.value
        self.t.update()

    
def main(page: Page):
    # create application instance
    my_input = MyInput()
    c1 = ft.Switch(label="Unchecked switch", value=False)
    # add application's root control to the page
    page.add(my_input, c1)
    
    
ft.app(target=main)