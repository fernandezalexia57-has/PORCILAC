import flet as ft

def reportes_form(regresar):
    # Campos de fecha para el reporte
    fecha_inicio_input = ft.TextField(
        label="Fecha de inicio",
        hint_text="AAAA/MM/DD",
        width=250,
        read_only=True
    )

    def seleccionar_fecha_inicio(e):
        if e.control.value:
            fecha_inicio_input.value = e.control.value.strftime("%Y/%m/%d")
            e.page.update()

    date_picker_inicio = ft.DatePicker(on_change=seleccionar_fecha_inicio)

    fecha_termino_input = ft.TextField(
        label="Fecha de término",
        hint_text="AAAA/MM/DD",
        width=250,
        read_only=True
    )

    def seleccionar_fecha_termino(e):
        if e.control.value:
            fecha_termino_input.value = e.control.value.strftime("%Y/%m/%d")
            e.page.update()

    date_picker_termino = ft.DatePicker(on_change=seleccionar_fecha_termino)

    tipo_reporte_dropdown = ft.Dropdown(
        label="Tipo de reporte",
        width=250,
        options=[
            ft.dropdown.Option("Mensual"),
            ft.dropdown.Option("Semanal"),
            ft.dropdown.Option("Anual")
        ],
        value="Mensual"
    )

    mensaje_reporte = ft.Text("", color=ft.Colors.GREEN)

    def generar_reporte(e):
        tipo = tipo_reporte_dropdown.value
        f_inicio = fecha_inicio_input.value
        f_termino = fecha_termino_input.value

        if not f_inicio or not f_termino:
            mensaje_reporte.value = "Seleccione las fechas de inicio y término"
            mensaje_reporte.color = ft.Colors.RED
        else:
            mensaje_reporte.value = f"Reporte '{tipo}' generado exitosamente del {f_inicio} al {f_termino}"
            mensaje_reporte.color = ft.Colors.GREEN
        e.page.update()

    # Tarjetas de Estadísticas Superiores
    def crear_tarjeta(titulo, valor, color_texto, icono_color):
        return ft.Container(
            width=210,
            padding=15,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            content=ft.Column(
                controls=[
                    ft.Text(titulo, size=14, color=ft.Colors.BLACK54, weight=ft.FontWeight.W_500),
                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.PETS, color=icono_color, size=30),
                            ft.Text(valor, size=24, color=color_texto, weight=ft.FontWeight.BOLD)
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                ],
                spacing=10
            )
        )

    tarjeta_preñadas = crear_tarjeta("Cerdas preñadas", "20", "#E85A8E", ft.Colors.PINK_300)
    tarjeta_partos = crear_tarjeta("Partos este mes", "8", "#3B82F6", ft.Colors.BLUE_300)
    tarjeta_destetados = crear_tarjeta("Lechones destetados", "78", "#10B981", ft.Colors.GREEN_300)
    tarjeta_mortalidad = crear_tarjeta("Mortalidad (%)", "2.1%", "#EF4444", ft.Colors.RED_300)

    # Gráfica simulada con barras de Flet (Nacidos vivos vs Destetados)
    grafica_container = ft.Container(
        width=450,
        height=320,
        padding=20,
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        content=ft.Column(
            controls=[
                ft.Text("Nacidos vivos vs Destetados", size=16, weight=ft.FontWeight.BOLD),
                ft.Row(
                    controls=[
                        ft.Row([ft.Container(width=10, height=10, bgcolor="#3B82F6", border_radius=5), ft.Text("Nacidos vivos", size=12)]),
                        ft.Row([ft.Container(width=10, height=10, bgcolor="#E85A8E", border_radius=5), ft.Text("Destetados", size=12)]),
                    ],
                    spacing=20
                ),
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                ft.Row(
                    controls=[
                        ft.Column([ft.Container(width=30, height=140, bgcolor="#3B82F6", border_radius=4), ft.Text("Mes 1", size=10)], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.Column([ft.Container(width=30, height=120, bgcolor="#E85A8E", border_radius=4), ft.Text("")], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.Column([ft.Container(width=30, height=150, bgcolor="#3B82F6", border_radius=4), ft.Text("Mes 2", size=10)], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.Column([ft.Container(width=30, height=160, bgcolor="#E85A8E", border_radius=4), ft.Text("")], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.Column([ft.Container(width=30, height=130, bgcolor="#3B82F6", border_radius=4), ft.Text("Mes 3", size=10)], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.Column([ft.Container(width=30, height=145, bgcolor="#E85A8E", border_radius=4), ft.Text("")], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    vertical_alignment=ft.CrossAxisAlignment.END,
                    expand=True
                )
            ],
            spacing=5
        )
    )

    return ft.Container(
        padding=30,
        expand=True,
        bgcolor=ft.Colors.GREY_50,
        content=ft.Column(
            controls=[
                ft.Text("Reportes", size=26, weight=ft.FontWeight.BOLD),
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                
                # Fila de tarjetas superiores
                ft.Row(
                    controls=[tarjeta_preñadas, tarjeta_partos, tarjeta_destetados, tarjeta_mortalidad],
                    spacing=15,
                    wrap=True
                ),
                
                ft.Divider(height=15, color=ft.Colors.TRANSPARENT),
                
                # Contenido inferior: Gráfica y Panel de Filtros
                ft.Row(
                    controls=[
                        grafica_container,
                        ft.Container(
                            width=320,
                            padding=20,
                            bgcolor=ft.Colors.WHITE,
                            border_radius=10,
                            content=ft.Column(
                                controls=[
                                    tipo_reporte_dropdown,
                                    fecha_inicio_input,
                                    ft.IconButton(icon=ft.Icons.CALENDAR_MONTH, on_click=lambda e: e.page.show_dialog(date_picker_inicio)),
                                    fecha_termino_input,
                                    ft.IconButton(icon=ft.Icons.CALENDAR_MONTH, on_click=lambda e: e.page.show_dialog(date_picker_termino)),
                                    date_picker_inicio,
                                    date_picker_termino,
                                    ft.ElevatedButton(
                                        "Generar reporte",
                                        icon=ft.Icons.PIE_CHART,
                                        bgcolor="#E85A8E",
                                        color=ft.Colors.WHITE,
                                        width=250,
                                        on_click=generar_reporte
                                    ),
                                    mensaje_reporte,
                                    ft.Row(
                                        controls=[
                                            ft.ElevatedButton("Exportar", icon=ft.Icons.DOWNLOAD, bgcolor=ft.Colors.GREEN_700, color=ft.Colors.WHITE),
                                            ft.ElevatedButton("Imprimir", icon=ft.Icons.PRINT, bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE),
                                        ],
                                        spacing=10
                                    )
                                ],
                                spacing=12
                            )
                        )
                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.START
                )
            ],
            spacing=10,
            scroll=ft.ScrollMode.AUTO
        )
    )