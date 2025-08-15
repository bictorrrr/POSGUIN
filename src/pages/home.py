import flet as ft
from constants import routes

def homeVista(page: ft.Page) -> ft.View:

    btInventario = ft.ElevatedButton(
        text="Inventario",
        width=300,
        height=300,
        bgcolor=ft.Colors.BLUE_300,
        color=ft.Colors.WHITE,
        on_click=lambda _: page.go(routes.LOGININVENTARIO)
    )

    btVentas = ft.ElevatedButton(
        text="Ventas",
        width=300,
        height=300,
        bgcolor=ft.Colors.BLUE_300,
        color=ft.Colors.WHITE
    )

    logo = ft.Image(
        src=f"posguin_logoandtittle.png", 
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN
    )

    return ft.View(
        route=routes.MAIN,
        controls=[
            ft.Column(
                controls=[
                    ft.Row(
                        [
                            ft.Text("Bienvenido a POSGUIN", size=30, weight=ft.FontWeight.BOLD),
                            logo,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [ft.Column([
                            ft.Text("A donde va?", size=30, weight=ft.FontWeight.BOLD),
                        ]
                        )],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Divider(height=100, visible=True),
                    ft.Row(
                        [
                            btInventario,
                            btVentas
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=50
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]
    )
