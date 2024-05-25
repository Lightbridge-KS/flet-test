import flet as ft


lookup_1 = ["Body", "Neuro"]

lookup_2 = {
    "Body": ["Red", "Green"],
    "Neuro": ["Blue"]
}

lookup_3 = {
    "Red": ["A"],
    "Green": ["B", "C"],
    "Blue": ["D", "E"]
}

def main(page: ft.Page):
    def dropdown_changed_1(e):
        t1.value = f"Dropdown 1 changed to {dd_1.value}"
        
        lookup_2_selected = lookup_2[dd_1.value]
        dd_2.options = [ft.dropdown.Option(x) for x in lookup_2_selected]
        page.update()
        
    def dropdown_changed_2(e):
        t2.value = f"Dropdown 2 changed to {dd_2.value}"
        
        lookup_3_selected = lookup_3[dd_2.value]
        dd_3.options = [ft.dropdown.Option(x) for x in lookup_3_selected]
        page.update()
    
    def dropdown_changed_3(e):
        t3.value = f"Dropdown 3 changed to {dd_3.value}"
        page.update()
    
    
    dd_1 = ft.Dropdown(
        options=[ft.dropdown.Option(x) for x in lookup_1],
        on_change=dropdown_changed_1
    )
    
    dd_2 = ft.Dropdown(
        on_change=dropdown_changed_2
    )
    
    dd_3 = ft.Dropdown(
        ## Uncomment for default value
        # options=[ft.dropdown.Option(x) for x in lookup_2["Red"]],
        on_change=dropdown_changed_3
    )
    
    t1 = ft.Text()
    t2 = ft.Text()
    t3 = ft.Text()
    
    page.add(dd_1, dd_2, dd_3, t1, t2, t3)
    

ft.app(target=main)