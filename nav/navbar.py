import flet as ft

def main(page: ft.Page):
    
	# GET INDEX TAB
    def change_tab(e):
        my_index = e.control.selected_index
        tab_1.visible = True if my_index == 0 else False
        tab_2.visible = True if my_index == 1 else False
        tab_3.visible = True if my_index == 2 else False
        page.update()


    page.title = "NavigationBar Example"
    page.navigation_bar = ft.NavigationBar(
        selected_index = 0,
        on_change= change_tab, # KEY
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Commute"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Explore",
            ),
        ]
    )
    
    tab_1 = ft.Text("Tab 1",size=30,visible=True)
    tab_2 = ft.Text("Tab 2",size=30,visible=False)
    tab_3 = ft.Text("Tab 3",size=30,visible=False)
 
    page.add(
        ft.Column([tab_1, tab_2, tab_3])
        )



ft.app(target=main)