from pages.home import homeVista
from pages.loginInventario import loginInventarioVista
from pages.inventario import inventarioVista
from pages.almacen import almacenVista
from constants import routes
import flet as ft

def main(page: ft.Page):
    page.title = "POSGUIN - Sistema de Administracion"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.maximized = True

    def route_change(route):
        page.views.clear()

        match page.route:
            case routes.MAIN:
                page.views.append(homeVista(page))
            case routes.LOGININVENTARIO:
                page.views.append(loginInventarioVista(page))
            case routes.INVENTARIO:
                page.views.append(inventarioVista(page))
            case routes.ALMACEN:
                page.views.append(almacenVista(page))
            # etc.

        page.update()

    page.on_route_change = route_change
    page.go(page.route)  
    page.go(routes.ALMACEN)

ft.app(target=main, assets_dir="assets")
