import flet as ft
from constants import routes
from db.db_manager import obtener_productos, obtener_productos_por_nombre
from popups.agregarProducto import crear_formulario_agregar_producto



def almacenVista(page: ft.Page) -> ft.View:

    def guardar_producto(e, page):
        dialog = crear_formulario_agregar_producto(page)
        page.open(dialog)

    def on_tab_change(e):
        update_content()
        page.update()
    
    def buscar_producto(e):
        nombre_producto = txBuscarProducto.value.strip()
        if nombre_producto:
            productos = obtener_productos_por_nombre(nombre_producto)
            tablaProductos.rows = [
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(p[0]))),  # codigo
                        ft.DataCell(ft.Text(p[1])),      # nombre
                        ft.DataCell(ft.Text(f"${p[2]:.2f}")),  # precio venta
                        ft.DataCell(ft.Text(f"${p[3]:.2f}")),  # precio compra
                        ft.DataCell(ft.Text(str(p[4]))),       # stock
                        ft.DataCell(
                            ft.Container(
                                bgcolor=ft.Colors.GREEN_200 if p[5] else ft.Colors.RED_200,
                                margin=ft.margin.symmetric(horizontal=5, vertical=2),
                                border_radius=10,
                                padding=ft.padding.symmetric(horizontal=10, vertical=5),
                                alignment=ft.alignment.center,
                                content=ft.Text(
                                    "Activo" if p[5] else "Inactivo",
                                    weight="bold",
                                    color=ft.Colors.GREEN_900 if p[5] else ft.Colors.RED_900,
                                    text_align=ft.TextAlign.CENTER,
                                )
                            )
                        ),
                        ft.DataCell(ft.IconButton(icon=ft.Icons.EDIT)),
                        ft.DataCell(ft.IconButton(icon=ft.Icons.REMOVE_RED_EYE_ROUNDED)),
                    ]
                )
                for p in productos
            ]
        else:
            update_content()
        page.update()

    def update_content():
        match tabs.selected_index:
            case 0:
                productos = obtener_productos()
                tablaProductos.rows = [
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(p[0]))),  # codigo
                            ft.DataCell(ft.Text(p[1])),      # nombre
                            ft.DataCell(ft.Text(f"${p[2]:.2f}")),  # precio venta
                            ft.DataCell(ft.Text(f"${p[3]:.2f}")),  # precio compra
                            ft.DataCell(ft.Text(str(p[4]))),       # stock
                            ft.DataCell(
                                ft.Container(
                                    bgcolor=ft.Colors.GREEN_200 if p[5] else ft.Colors.RED_200,
                                    margin=ft.margin.symmetric(horizontal=5, vertical=2),
                                    border_radius=10,
                                    padding=ft.padding.symmetric(horizontal=10, vertical=5),
                                    alignment=ft.alignment.center,
                                    content=ft.Text(
                                        "Activo" if p[5] else "Inactivo",
                                        weight="bold",
                                        color=ft.Colors.GREEN_900 if p[5] else ft.Colors.RED_900,
                                        text_align=ft.TextAlign.CENTER,
                                    )
                                )
                            ),
                            ft.DataCell(ft.IconButton(icon=ft.Icons.EDIT)),
                            ft.DataCell(ft.IconButton(icon=ft.Icons.REMOVE_RED_EYE_ROUNDED)),
                        ]
                    )
                    for p in productos
                ]
                content_container.content = ft.Column(
                    expand=True,
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Row(
                            controls=[
                                txBuscarProducto,
                                btAgregarProducto,
                                btGuardarReporte,
                            ],
                        ),
                        ft.Container(
                            expand=True,
                            alignment=ft.alignment.top_center,
                            content=ft.Column(
                                expand=True,
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.Container(
                                        expand=True,
                                        alignment=ft.alignment.top_center,
                                        content=ft.Row(
                                            expand=True,
                                            controls=[
                                                ft.Container(
                                                    expand=True,
                                                    alignment=ft.alignment.top_center,
                                                    content=ft.Column(
                                                        expand=True,
                                                        scroll=ft.ScrollMode.ALWAYS,
                                                        alignment=ft.MainAxisAlignment.START,
                                                        controls=[
                                                            tablaProductos
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )

            case 1:
                content_container.content = ft.Column([
                    ft.Text("📂 Categorías", size=18, weight="bold"),
                    ft.Text("Aquí puedes ver y organizar las categorías de productos."),
                ])
            case 2:
                content_container.content = ft.Column([
                    ft.Text("🔄 Entradas de inventario", size=18, weight="bold"),
                    ft.Text("Aquí puedes registrar los movimientos de inventario."),
                ])

    # Definimos las pestañas (sin contenido directo)
    selected_tab_index = ft.Ref[int]()  # Referencia para saber cuál pestaña está activa

    # Contenedor donde se mostrará el contenido dinámico
    content_container = ft.Container(expand=1, padding=20)

    txBuscarProducto = ft.TextField(label="Buscar Producto",
                                         width=300,
                                         hint_text="Ej. Coca Cola 600ml",
                                         prefix_icon=ft.Icons.SEARCH,
                                         expand=4,
                                         
                                         )
    txBuscarProducto.on_change = buscar_producto  # Evento al cambiar el texto
    
    btAgregarProducto = ft.ElevatedButton(text="Agregar Producto", 
                                              icon=ft.Icons.ADD,
                                              expand=1,
                                              height=50,
                                              on_click=lambda _, pagina=page: guardar_producto(_, pagina))
    
    btGuardarReporte = ft.ElevatedButton(text="Guardar Reporte",
                                              icon=ft.Icons.SAVE,
                                              expand=1,
                                              height=50,)

    tablaProductos = ft.DataTable(
                                columns=[
                                    ft.DataColumn(ft.Text("Codigo")),
                                    ft.DataColumn(ft.Text("Nombre", expand=True)),
                                    ft.DataColumn(ft.Text("Precio Venta")),
                                    ft.DataColumn(ft.Text("Precio Compra")),
                                    ft.DataColumn(ft.Text("Stock")),
                                    ft.DataColumn(ft.Text("Status")),
                                    ft.DataColumn(ft.Text("Editar")),
                                    ft.DataColumn(ft.Text("Ver")),
                                ], expand=True,
                                    
                            )
    tabs = ft.Tabs(
        selected_index=0,
        on_change=on_tab_change, 
        ref=selected_tab_index,
        tabs=[
            ft.Tab(text="PRODUCTOS", icon=ft.icons.INVENTORY_2,),
            ft.Tab(text="CATEGORIAS", icon=ft.icons.CATEGORY),
            ft.Tab(text="ENTRADAS DE INVENTARIO", icon=ft.icons.SWAP_HORIZ),
        ],
        expand=True,
        visible=True,
        
    )

    logo = ft.Image(
        src=f"posguin_onlylogo.png", 
        width=50,
        height=50,
        fit=ft.ImageFit.CONTAIN
    )

    update_content()

    return ft.View(
        route=routes.ALMACEN,
        controls=[
            ft.Column(
                expand=True,
                controls=[
                    ft.Container(
                        bgcolor=ft.Colors.BLUE_50,
                        padding=20,
                        content=ft.Row(
                            controls=[
                                logo,
                                ft.Text("Almacén", size=22, weight="bold", color=ft.Colors.BLUE_800),
                                ft.VerticalDivider(width=20, visible=True),
                                tabs,
                                ft.ElevatedButton(
                                    text="Regresar a Inventario",
                                    height=50,
                                    bgcolor=ft.Colors.RED_300,
                                    color=ft.Colors.WHITE,
                                    on_click=lambda _: page.go("/inventario"),
                                    icon=ft.icons.ARROW_BACK_IOS,
                                    icon_color=ft.Colors.WHITE,
                                )
                            ],
                            alignment=ft.MainAxisAlignment.START
                        )
                    ),

                    content_container
                ]
            )
        ]
    )
