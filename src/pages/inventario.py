import flet as ft
from constants.routes import INVENTARIO

def inventarioVista(page: ft.Page) -> ft.View:

    def on_nav_change(e):
        selected = e.control.selected_index
        print("Ítem seleccionado:", selected)
        match selected:
            case 0:
                page.go("/inventario/almacen")
            case 1:
                print("Navegando a Clientes")
            case 2:
                print("Navegando a Proveedores")
            case 3:
                print("Navegando a Cotizaciones")
            case _:
                print("Ningún ítem seleccionado")

    return ft.View(
        route=INVENTARIO,
        controls=[
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Usuario: POSGUIN JR", size=16, weight="bold", color=ft.Colors.BLUE_800),
                                ft.Divider(height=10, thickness=1),
                                ft.NavigationRail(
                                    selected_index=0,
                                    label_type=ft.NavigationRailLabelType.ALL,
                                    destinations=[
                                        ft.NavigationRailDestination(icon=ft.icons.WAREHOUSE, label="Almacén"),
                                        ft.NavigationRailDestination(icon=ft.icons.PEOPLE, label="Clientes"),
                                        ft.NavigationRailDestination(icon=ft.icons.LOCAL_SHIPPING, label="Proveedores"),
                                        ft.NavigationRailDestination(icon=ft.icons.DESCRIPTION, label="Cotizaciones"),
                                    ],
                                    extended=True,
                                    bgcolor=ft.Colors.BLUE_100,
                                    on_change=on_nav_change,
                                    expand=True
                                ),
                                ft.Divider(height=10, thickness=1),
                                ft.Row([
                                    ft.ElevatedButton(
                                    text="Cerrar Sesión/Salir",
                                    height=40,
                                    bgcolor=ft.Colors.RED_300,
                                    color=ft.Colors.WHITE,
                                    on_click=lambda _: page.go("/login/inventario"),
                                    expand=True
                                )
                                ])
                            ],
                            spacing=15,
                            expand=True
                        ),
                        bgcolor=ft.Colors.BLUE_50,
                        expand=1,
                        padding=20
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("CONTENIDO PRINCIPAL", size=30, weight="bold"),
                            # Más contenido aquí
                        ]),
                        expand=4,
                        padding=20
                    ),
                ],
                expand=True
            )
        ]
    )
