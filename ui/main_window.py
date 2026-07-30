import flet as ft 

from ui.cerda_from import cerda_form
from ui.destete_from import destete_form
from ui.usuarios_from import usuarios_form
from ui.reportes_from import reportes_form  # Importación del módulo de reportes

def main_window(page: ft.Page):
    page.title = "Sistema de Gestion de Reproduccion de Cerdas"
    page.window_width = 1100
    page.window_height = 700
    page.padding = 0
    page.bgcolor = ft.Colors.WHITE

    # Ejemplo de widget: Text
    titulo = ft.Text(
        "Sistema de Gestion de Reproduccion de Cerdas",
        size=24,
        weight=ft.FontWeight.BOLD
    )

    subtitulo = ft.Text(
        "Seleccione una opción del menú",
        size=16,
        color=ft.Colors.PINK_400
    )

    # Widget Container (Declarado primero para que las funciones lo reconozcan)
    contenido = ft.Container(
        padding=30,
        expand=True
    )

    def inicio():
        return ft.Column(
            controls=[
                titulo, 
                subtitulo
            ],
            spacing=10
        )

    def mostrar_inicio(e=None):
        contenido.content = inicio()
        page.update()

    def mostrar_cerdas(e=None):
        contenido.content = cerda_form(mostrar_inicio)
        page.update()

    def mostrar_destete(e=None):
        contenido.content = destete_form(mostrar_inicio)
        page.update()

    def mostrar_empleados(e=None):
        contenido.content = usuarios_form(mostrar_inicio)
        page.update()

    def mostrar_reportes(e=None):
        contenido.content = reportes_form(mostrar_inicio)
        page.update()

    menu_lateral = ft.Container(
        width=220,
        bgcolor=ft.Colors.PINK_300,
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text(
                    "PORCILAC",  
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),
                ft.Text(
                    "Sistema de gestión",
                    size=12,
                    color=ft.Colors.PINK_700
                ),
                ft.Divider(color=ft.Colors.PINK_700),
                ft.ElevatedButton(
                    "Inicio",
                    icon=ft.Icons.HOME_FILLED,
                    width=180,
                    color=ft.Colors.BLACK,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=2),
                    ),
                    on_click=mostrar_inicio
                ),
                ft.ElevatedButton(
                    "Empleados",
                    icon=ft.Icons.PEOPLE_ALT_OUTLINED,
                    width=180,
                    color=ft.Colors.BLACK,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=2),
                    ),
                    on_click=mostrar_empleados
                ),
                ft.ElevatedButton(
                    "🐷Cerdas",
                    icon="TAG_FACES",
                    width=180,
                    color=ft.Colors.BLACK,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=2),
                    ),
                    on_click=mostrar_cerdas
                ),
                ft.ElevatedButton(
                    "Reproducción",
                    icon=ft.Icons.SWAP_HORIZ,
                    width=180,
                    color=ft.Colors.BLACK,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=2),
                    ),
                    on_click=mostrar_inicio
                ),
                ft.ElevatedButton(
                    "Partos",
                    icon=ft.Icons.CHILD_CARE,
                    width=180,
                    color=ft.Colors.BLACK,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=2),
                    ),
                    on_click=mostrar_inicio
                ),
                ft.ElevatedButton(
                    "Destete",
                    icon=ft.Icons.OUTBOX,
                    width=180,
                    color=ft.Colors.BLACK,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=2),
                    ),
                    on_click=mostrar_destete
                ),
                ft.ElevatedButton(
                    "Reportes",
                    icon=ft.Icons.ASSESSMENT_OUTLINED,
                    width=180,
                    color=ft.Colors.BLACK,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=2),
                    ),
                    on_click=mostrar_reportes
                )                
            ],
            spacing=15
        )
    )
    
    layout = ft.Row(
        controls=[
            menu_lateral, 
            contenido
        ],
        expand=True
    )

    page.add(layout)
    mostrar_inicio()