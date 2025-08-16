import flet as ft

def contador_visual(valor_inicial=1, on_change=None, nombre = "contador", soloLectura=False):
    campo = ft.TextField(
        label=nombre,
        value=str(valor_inicial),
        width=100,
        text_align=ft.TextAlign.CENTER,
        read_only=soloLectura,
    )

    def sumar(e):
        campo.value = str(int(campo.value) + 1)
        if on_change:
            on_change(int(campo.value))
        campo.update()

    def restar(e):
        campo.value = str(max(0, int(campo.value) - 1))
        if on_change:
            on_change(int(campo.value))
        campo.update()

    return ft.Row([
        ft.IconButton(ft.icons.REMOVE, on_click=restar),
        campo,
        ft.IconButton(ft.icons.ADD, on_click=sumar),
    ])
