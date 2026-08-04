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

    # Campos de fecha con el icono de calendario INTEGRADO DENTRO del campo
    fecha_inicio_input = ft.TextField(
        label="Fecha de inicio",
        hint_text="AAAA/MM/DD",
        expand=True,
        read_only=True,
        border_radius=8,
        bgcolor=ft.Colors.WHITE,
        suffix_icon=ft.Icons.CALENDAR_MONTH
    )

    def seleccionar_fecha_inicio(e):
        if e.control.value:
            fecha_inicio_input.value = e.control.value.strftime("%Y/%m/%d")
            e.page.update()

    date_picker_inicio = ft.DatePicker(on_change=seleccionar_fecha_inicio)

    fecha_termino_input = ft.TextField(
        label="Fecha de término",
        hint_text="AAAA/MM/DD",
        expand=True,
        read_only=True,
        border_radius=8,
        bgcolor=ft.Colors.WHITE,
        suffix_icon=ft.Icons.CALENDAR_MONTH
    )

    def seleccionar_fecha_termino(e):
        if e.control.value:
            fecha_termino_input.value = e.control.value.strftime("%Y/%m/%d")
            e.page.update()

    date_picker_termino = ft.DatePicker(on_change=seleccionar_fecha_termino)

    tipo_reporte_dropdown = ft.Dropdown(
        label="Tipo de reporte",
        expand=True,
        options=[
            ft.dropdown.Option("Mensual"),
            ft.dropdown.Option("Semanal"),
            ft.dropdown.Option("Anual")
        ],
        value="Mensual",
        border_radius=8,
        bgcolor=ft.Colors.WHITE
    )

    mensaje_reporte = ft.Text("", size=13)

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
                    mensaje_reporte.value = f"Reporte '{tipo}' guardado con éxito"
                    mensaje_reporte.color = ft.Colors.GREEN
                else:
                    mensaje_reporte.value = "Error al guardar en la base de datos"
                    mensaje_reporte.color = ft.Colors.RED
            except Exception as err:
                print("Error detallado al generar reporte:", err)
                mensaje_reporte.value = "Ocurrió un error inesperado"
                mensaje_reporte.color = ft.Colors.RED
                
        e.page.update()

    # --- TARJETAS SUPERIORES MÁS ANCHAS ---
    def crear_tarjeta(titulo, valor, icono, color):
        return ft.Container(
            expand=True,
            height=110,
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            shadow=ft.BoxShadow(spread_radius=1, blur_radius=8, color=ft.Colors.BLACK12),
            content=ft.Column(
                controls=[
                    ft.Text(titulo, size=14, color=ft.Colors.BLACK54, weight=ft.FontWeight.W_500),
                    ft.Row(
                        controls=[
                            ft.Icon(icono, color=color, size=32),
                            ft.Text(valor, size=26, color=color, weight=ft.FontWeight.BOLD)
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ],
                spacing=8,
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    tarjeta_preñadas = crear_tarjeta("Cerdas preñadas", "20", ft.Icons.SAVINGS, ft.Colors.PINK_400)
    tarjeta_partos = crear_tarjeta("Partos este mes", "8", ft.Icons.SAVINGS, ft.Colors.BLUE_600)
    tarjeta_destetados = crear_tarjeta("Lechones destetados", total_lechones_real, ft.Icons.SAVINGS, ft.Colors.GREEN_600)
    tarjeta_mortalidad = crear_tarjeta("Mortalidad (%)", "2.1%", ft.Icons.SAVINGS, ft.Colors.RED_700)

    # --- GRÁFICA SÚPER AMPLIADA (ocupa todo el ancho restante y más altura) ---
    grafica_container = ft.Container(
        expand=True,  # Se expande para ocupar todo el ancho disponible a la izquierda
        height=480,   # Mucho más alta
        padding=30,
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=8, color=ft.Colors.BLACK12),
        content=ft.Column(
            controls=[
                ft.Text("Nacidos vivos vs Destetados", size=20, weight=ft.FontWeight.BOLD),
                ft.Row(
                    controls=[
                        ft.Row([ft.Container(width=14, height=14, bgcolor="#3B82F6", border_radius=7), ft.Text("Nacidos vivos", size=14)]),
                        ft.Row([ft.Container(width=14, height=14, bgcolor="#E85A8E", border_radius=7), ft.Text("Destetados", size=14)]),
                    ],
                    spacing=30
                ),
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                ft.Row(
                    controls=[
                        ft.Column([ft.Container(width=55, height=240, bgcolor="#3B82F6", border_radius=8), ft.Text("Mes 1", size=13, weight=ft.FontWeight.W_500)], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.Column([ft.Container(width=55, height=200, bgcolor="#E85A8E", border_radius=8), ft.Text("")], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.Column([ft.Container(width=55, height=270, bgcolor="#3B82F6", border_radius=8), ft.Text("Mes 2", size=13, weight=ft.FontWeight.W_500)], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.Column([ft.Container(width=55, height=230, bgcolor="#E85A8E", border_radius=8), ft.Text("")], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.Column([ft.Container(width=55, height=300, bgcolor="#3B82F6", border_radius=8), ft.Text("Mes 3", size=13, weight=ft.FontWeight.W_500)], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.Column([ft.Container(width=55, height=255, bgcolor="#E85A8E", border_radius=8), ft.Text("")], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    vertical_alignment=ft.CrossAxisAlignment.END,
                    expand=True
                )
            ],
            spacing=15,
            expand=True
        )
    )

    # Botones de Exportar e Imprimir más grandes
    btn_exportar = ft.ElevatedButton(
        "Exportar", 
        icon=ft.Icons.DOWNLOAD, 
        bgcolor=ft.Colors.GREEN_700, 
        color=ft.Colors.WHITE,
        height=45,
        expand=True
    )
    
    btn_imprimir = ft.ElevatedButton(
        "Imprimir", 
        icon=ft.Icons.PRINT, 
        bgcolor=ft.Colors.GREEN_700, 
        color=ft.Colors.WHITE,
        height=45,
        expand=True
    )

    # --- PANEL DE CONFIGURACIÓN DE REPORTE AMPLIADO (ancho fijo grande y altura acorde a la gráfica) ---
    panel_filtros = ft.Container(
        width=440,  # Más ancho
        height=480, # Misma altura grande que la gráfica
        padding=30,
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=8, color=ft.Colors.BLACK12),
        content=ft.Column(
            controls=[
                ft.Text("Configuración de Reporte", size=18, weight=ft.FontWeight.BOLD),
                tipo_reporte_dropdown,
                
                ft.Container(
                    content=fecha_inicio_input,
                    on_click=lambda e: e.page.open(date_picker_inicio)
                ),
                
                ft.Container(
                    content=fecha_termino_input,
                    on_click=lambda e: e.page.open(date_picker_termino)
                ),
                
                date_picker_inicio,
                date_picker_termino,
                
                ft.ElevatedButton(
                    "Generar reporte",
                    icon=ft.Icons.BAR_CHART,
                    bgcolor="#E85A8E",
                    color=ft.Colors.WHITE,
                    height=50,
                    expand=True,
                    on_click=generar_reporte
                ),
                mensaje_reporte,
                ft.Row(
                    controls=[btn_exportar, btn_imprimir],
                    spacing=15,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    return ft.Container(
        padding=30,
        expand=True,
        bgcolor=ft.Colors.GREY_50,
        content=ft.Column(
            controls=[
                ft.Text("Reportes", size=28, weight=ft.FontWeight.BOLD),
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                
                # Fila superior de los 4 bloques anchos
                ft.Row(
                    controls=[tarjeta_preñadas, tarjeta_partos, tarjeta_destetados, tarjeta_mortalidad],
                    spacing=20,
                    expand=False
                ),
                
                ft.Divider(height=15, color=ft.Colors.TRANSPARENT),
                
                # Fila inferior con gráfica expandida y panel de filtros grande ocupando toda la pantalla
                ft.Row(
                    controls=[grafica_container, panel_filtros],
                    spacing=25,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    expand=True
                )
            ],
            spacing=10,
            expand=True,
            scroll=ft.ScrollMode.AUTO
        )
    )