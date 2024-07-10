import flet as ft

class MyDropDown(ft.UserControl):
    def __init__(self, width=100, options=None):
        super().__init__()
        self.width = width
        self.options = options or []

    def build(self):
        self.t = ft.Text()
        self.b = ft.ElevatedButton(text="Submit", on_click=self.button_clicked)
        self.dd = ft.Dropdown(width=self.width, options=self.options)
        return ft.Column([self.dd, self.b, self.t])

    def button_clicked(self, e):
        self.t.value = f"Dropdown value is: {self.dd.value}"
        self.update()
        
        

if __name__ == "__main__":
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