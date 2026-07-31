import flet as ft
from dao.destete_dao import DesteteDAO
from dao.reportes_dao import ReportesDAO

def reportes_form(regresar):
    
    # --- CONSULTAR DATOS REALES DE LA BASE DE DATOS ---
    total_lechones_real = "0"
    try:
        destete_dao = DesteteDAO()
        destetes = destete_dao.obtener_todos()
        total_lechones_real = str(sum(d.numLechones for d in destetes))
    except Exception as e:
        print("Error al obtener los destetes para el reporte:", e)

    # Campos de fecha para el reporte
    fecha_inicio_input = ft.TextField(
        label="Fecha de inicio",
        hint_text="AAAA/MM/DD",
        width=280,
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
        width=280,
        read_only=True
    )

    def seleccionar_fecha_termino(e):
        if e.control.value:
            fecha_termino_input.value = e.control.value.strftime("%Y/%m/%d")
            e.page.update()

    date_picker_termino = ft.DatePicker(on_change=seleccionar_fecha_termino)

    tipo_reporte_dropdown = ft.Dropdown(
        label="Tipo de reporte",
        width=280,
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
            try:
                reporte_dao = ReportesDAO()
                exito = reporte_dao.insertar(
                    tipo=tipo, 
                    fecha_inicio=f_inicio, 
                    fecha_termino=f_termino, 
                    cerdas_prenadas=20, 
                    partos_mes=8, 
                    lechones_destetados=int(total_lechones_real), 
                    mortalidad=2.1
                )
                
                if exito:
                    mensaje_reporte.value = f"Reporte '{tipo}' generado y guardado en la BD"
                    mensaje_reporte.color = ft.Colors.GREEN
                else:
                    mensaje_reporte.value = "Error al guardar el reporte en la base de datos"
                    mensaje_reporte.color = ft.Colors.RED
            except Exception as err:
                print("Error detallado al generar reporte:", err)
                mensaje_reporte.value = "Ocurrió un error inesperado al guardar"
                mensaje_reporte.color = ft.Colors.RED
                
        e.page.update()

    # --- TARJETAS SUPERIORES ---
    tarjeta_preñadas = ft.Container(
        width=210, height=95, padding=15, bgcolor=ft.Colors.WHITE, border_radius=10,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=5, color=ft.Colors.GREY_300),
        content=ft.Column(controls=[
            ft.Text("Cerdas preñadas", size=13, color=ft.Colors.BLACK54, weight=ft.FontWeight.W_500),
            ft.Row(controls=[
                ft.Icon(ft.Icons.SAVINGS, color=ft.Colors.PINK_400, size=28),
                ft.Text("20", size=22, color=ft.Colors.PINK_400, weight=ft.FontWeight.BOLD)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER)
        ], spacing=5)
    )

    tarjeta_partos = ft.Container(
        width=210, height=95, padding=15, bgcolor=ft.Colors.WHITE, border_radius=10,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=5, color=ft.Colors.GREY_300),
        content=ft.Column(controls=[
            ft.Text("Partos este mes", size=13, color=ft.Colors.BLACK54, weight=ft.FontWeight.W_500),
            ft.Row(controls=[
                ft.Icon(ft.Icons.SAVINGS, color=ft.Colors.BLUE_600, size=28),
                ft.Text("8", size=22, color=ft.Colors.BLUE_600, weight=ft.FontWeight.BOLD)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER)
        ], spacing=5)
    )

    tarjeta_destetados = ft.Container(
        width=210, height=95, padding=15, bgcolor=ft.Colors.WHITE, border_radius=10,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=5, color=ft.Colors.GREY_300),
        content=ft.Column(controls=[
            ft.Text("Lechones destetados", size=13, color=ft.Colors.BLACK54, weight=ft.FontWeight.W_500),
            ft.Row(controls=[
                ft.Icon(ft.Icons.SAVINGS, color=ft.Colors.GREEN_600, size=28),
                ft.Text(total_lechones_real, size=22, color=ft.Colors.GREEN_600, weight=ft.FontWeight.BOLD)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER)
        ], spacing=5)
    )

    tarjeta_mortalidad = ft.Container(
        width=210, height=95, padding=15, bgcolor=ft.Colors.WHITE, border_radius=10,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=5, color=ft.Colors.GREY_300),
        content=ft.Column(controls=[
            ft.Text("Mortalidad (%)", size=13, color=ft.Colors.BLACK54, weight=ft.FontWeight.W_500),
            ft.Row(controls=[
                ft.Icon(ft.Icons.SAVINGS, color=ft.Colors.RED_700, size=28),
                ft.Text("2.1%", size=22, color=ft.Colors.RED_700, weight=ft.FontWeight.BOLD)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER)
        ], spacing=5)
    )

    # Gráfica simulada con barras de Flet
    grafica_container = ft.Container(
        width=480,
        height=330,
        padding=20,
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=5, color=ft.Colors.GREY_300),
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

    # Botones de Exportar e Imprimir
    btn_exportar = ft.ElevatedButton(
        "Exportar", 
        icon=ft.Icons.DOWNLOAD, 
        bgcolor=ft.Colors.GREEN_700, 
        color=ft.Colors.WHITE,
        width=134
    )
    
    btn_imprimir = ft.ElevatedButton(
        "Imprimir", 
        icon=ft.Icons.PRINT, 
        bgcolor=ft.Colors.GREEN_700, 
        color=ft.Colors.WHITE,
        width=134
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
                    wrap=False
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
                            shadow=ft.BoxShadow(spread_radius=1, blur_radius=5, color=ft.Colors.GREY_300),
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
                                        icon=ft.Icons.BAR_CHART,
                                        bgcolor="#E85A8E",
                                        color=ft.Colors.WHITE,
                                        width=280,
                                        on_click=generar_reporte
                                    ),
                                    mensaje_reporte,
                                    ft.Row(
                                        controls=[btn_exportar, btn_imprimir],
                                        spacing=12,
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
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