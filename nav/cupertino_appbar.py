import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    page.appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        bgcolor=ft.colors.SURFACE_VARIANT,
        trailing=ft.Icon(ft.icons.WB_SUNNY_OUTLINED),
      middle=ft.Text("CupertinoAppBar Example"),
    )
    page.add(ft.Text("Body!"))


ft.app(target=main)