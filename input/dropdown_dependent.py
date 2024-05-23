import flet as ft

lookup_1 = ["Red", "Green", "Blue"]
lookup_2 = {
    "Red": ["A"],
    "Green": ["B", "C"],
    "Blue": ["D", "E"]
}

def main(page: ft.Page):
    def dropdown_changed_1(e):
        # Update Dropdown 2 choices
        dd_2_lookup = lookup_2[dd_1.value]
        dd_2.options = [ft.dropdown.Option(x) for x in dd_2_lookup]
        
        t.value = f"Dropdown 1 changed to {dd_1.value}"
        page.update()
    
    def dropdown_changed_2(e):
        t2.value = f"Dropdown 2 changed to {dd_2.value}"
        page.update()
    
    dd_1 = ft.Dropdown(
        width=100,
        options=[ft.dropdown.Option(x) for x in lookup_1],
        on_change=dropdown_changed_1
    )
    
    dd_2 = ft.Dropdown(
        width=100,
        options=[ft.dropdown.Option(x) for x in lookup_2["Red"]],
        on_change=dropdown_changed_2
    )
    
    t = ft.Text()
    t2 = ft.Text()
    
    page.add(dd_1, dd_2, t, t2)
    

ft.app(target=main)