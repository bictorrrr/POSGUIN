
import flet as ft
from constants.routes import LOGININVENTARIO, INVENTARIO

def loginInventarioVista(page: ft.Page) -> ft.View:

    usuario = ft.TextField(label="Usuario", autofocus=True, width=300)
    contrasena = ft.TextField(label="Contraseña", password=True, width=300)


    return ft.View(
        route=LOGININVENTARIO,
        controls=[
            ft.Column([
                ft.Text("Inicio de Sesion", size=30, weight="bold"),
                ft.Text("Bienvenido, por favor ingrese sus credenciales para continuar.", size=20),
                ft.Divider(height=20, visible=True),
                usuario,
                contrasena,
                ft.ElevatedButton(
                    text="Ingresar a Inventario",
                    width=300,
                    height=50,
                    bgcolor=ft.Colors.BLUE_300,
                    color=ft.Colors.WHITE,
                    on_click=lambda _: page.go(INVENTARIO)
                ),
                ft.ElevatedButton(
                    text="Cancelar/Regresar a Inicio",
                    width=300,
                    height=50,
                    bgcolor=ft.Colors.RED_300,
                    color=ft.Colors.WHITE,
                    on_click=lambda _: page.go("/") 
                )


            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=20),
        ],
        vertical_alignment="center",
        horizontal_alignment="center",
    )