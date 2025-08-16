import flet as ft
from custom_controls.counter import contador_visual

def crear_formulario_agregar_producto(page: ft.Page):
   # Campos del formulario
    tf_id = ft.TextField(label="ID del producto", value="AUTOGENERADO", read_only=True, expand=1)
    tf_nombre = ft.TextField(label="Nombre del producto *", expand=True)
    tf_codigo = ft.TextField(label="Código", hint_text="Escanee el codigo...", autofocus=True, expand=1)
    cb_categoria = ft.Dropdown(label="Categoría", options=[ft.dropdown.Option("Bebidas"), ft.dropdown.Option("Alimentos")], expand=True)
    cb_proveedor = ft.Dropdown(label="Proveedor", options=[ft.dropdown.Option("Proveedor 1"), ft.dropdown.Option("Proveedor 2")], expand=True)

    c_stock = contador_visual(valor_inicial=0, nombre="Stock")
    c_stock_minimo = contador_visual(valor_inicial=0, nombre="Stock Mínimo")
    c_precio_compra = contador_visual(valor_inicial=0, nombre="Precio Compra")
    c_precio_venta = contador_visual(valor_inicial=0, nombre="Precio Venta")
    c_precio_venta_mayor = contador_visual(valor_inicial=0, nombre="Precio Venta Mayor")

    tf_unidad = ft.TextField(label="Unidad de medida", hint_text="Ej. Unidad")



    # Acción del botón Guardar
    def guardar_click(e):
        datos = {
            "nombre": tf_nombre.value,
            "codigo": tf_codigo.value,
            
        }

    dialog = ft.BottomSheet(
        content=ft.Container(
            ft.Column([
            ft.Row([
                tf_id, tf_codigo
            ]),
            ft.Row([
                tf_nombre   
            ]),
            ft.Row([
                 cb_categoria
            ]),
            ft.Row([
                cb_proveedor
            ]),
            ft.Row([
                c_stock, c_stock_minimo
            ]),
            ft.Row([
                c_precio_compra, c_precio_venta
            ]),
            ft.Row([
                c_precio_venta_mayor, tf_unidad
            ]),
            ft.TextButton("Cancelar", on_click=lambda e, page=page: page.close(form))
            
        ], expand=True), padding=10, width=600
        ), size_constraints=ft.BoxConstraints( min_width=1000)
        
    )

    # Crear el diálogo
    form = ft.AlertDialog(
        modal=True,
        title=ft.Text("Agregar nuevo producto"),
        content=ft.Container(
            ft.Column([
            ft.Row([
                tf_id, tf_codigo
            ]),
            ft.Divider(height=10, visible=True),
            ft.Row([
                tf_nombre   
            ]),
            ft.Divider(height=10, visible=True),
            ft.Row([
                 cb_categoria, c_stock, c_stock_minimo
            ]),
            ft.Divider(height=10, visible=True),
            ft.Row([
                cb_proveedor, c_precio_compra, c_precio_venta
            ]),
            ft.Divider(height=10, visible=True),
            ft.Row([
                c_precio_venta_mayor, tf_unidad
            ])
            
        ],scroll="adaptive"), width=700
        ),
        actions=[
            ft.TextButton("Cancelar", on_click=lambda e, page=page: page.close(form)),
            ft.ElevatedButton("Guardar", on_click=guardar_click),
        ]
    )

    return form
