import flet as ft


from ui.cerda_from import cerda_form

def main_window(page: ft.Page):
    page.title = "Sistema de Gestion de Reproduccion de Cerdas"
    page.window_width = 1100
    page.window_height = 700
    page.padding = 0
    page.bgcolor = ft.Colors.WHITE

    #Ejemplo de widget: Text
    titulo = ft.Text(
    "Sistema de Gestion de Reproduccion de Cerdas",
    size= 24,
    weight=ft.FontWeight.BOLD
    )

    subtitulo = ft.Text(
        "Seleccione una opción del menú",
        size= 16,
        color = ft.Colors.PINK_400
    )


    # Widget Container
    contenido = ft.Container(
        padding = 30,
        expand = True
    )

    def inicio():
        return ft.Column(
        controls= [
            titulo, 
            subtitulo
        ],
        spacing= 10
    )

    def mostrar_inicio(e=None):
        contenido.content = inicio()
        page.update()
            
    #Reacciona al click del botón de libros en el menú lateral
    def mostrar_insertar_cerda(e=None):
        contenido.content = cerda_form(mostrar_inicio)
        page.update()

   # def mostrar_lista_libros(e=None):
        #contenido.content = libros_list(mostrar_inicio)
        #page.update()

    menu_lateral = ft.Container(
        width = 220,
        bgcolor = ft.Colors.PINK_300,
        padding = 20,
        content = ft.Column(
            controls = [
                ft.Text(
                    "Granja",  
                    size = 22,
                    weight = ft.FontWeight.BOLD,
                    color = ft.Colors.WHITE
                ),
                ft.Text(
                    "Sistema de gestión",
                    size = 12,
                    color = ft.Colors.PINK_700
                ),
                ft.Divider(color = ft.Colors.PINK_700),
                ft.ElevatedButton(
                    "Inicio",
                    icon = ft.Icons.HOME,
                    width = 180,
                    color = ft.Colors.BLACK,
                    style = ft.ButtonStyle(
                        shape = ft.RoundedRectangleBorder(radius = 2),
                    ),
                  
                ),
                ft.ElevatedButton(
                    "Empleados",
                    icon = ft.Icons.PEOPLE,
                    width = 180,
                    color = ft.Colors.BLACK,
                    style = ft.ButtonStyle(
                        shape = ft.RoundedRectangleBorder(radius = 2),
                    ),
                    on_click = mostrar_inicio
                ),
                ft.ElevatedButton(
                    "🐷Cerdas",
                    icon = "🐷",
                    width = 180,
                    color = ft.Colors.BLACK,
                    style = ft.ButtonStyle(
                        shape = ft.RoundedRectangleBorder(radius = 2),
                    ),
                    on_click = mostrar_insertar_cerda
                ),
                ft.ElevatedButton(
                    "Reprodcción",
                    icon = ft.Icons.SWAP_HORIZ,
                    width = 180,
                    color = ft.Colors.BLACK,
                    style = ft.ButtonStyle(
                        shape = ft.RoundedRectangleBorder(radius = 2),
                    ),
                   
                ),
                ft.ElevatedButton(
                    "Partos",
                    icon = ft.Icons.KEYBOARD_RETURN,
                    width = 180,
                    color = ft.Colors.BLACK,
                    style = ft.ButtonStyle(
                        shape = ft.RoundedRectangleBorder(radius = 2),
                    ),
                 
                ),
                ft.ElevatedButton(
                    "Destete",
                    icon = ft.Icons.CHILD_CARE,
                    width = 180,
                    color = ft.Colors.BLACK,
                    style = ft.ButtonStyle(
                        shape = ft.RoundedRectangleBorder(radius = 2),
                    ),
                 
                ),
                ft.ElevatedButton(
                    "Reportes",
                    icon = ft.Icons.INSIGHTS,
                    width = 180,
                    color = ft.Colors.BLACK,
                    style = ft.ButtonStyle(
                        shape = ft.RoundedRectangleBorder(radius = 2),
                    ),
                
                )                
            ],
            spacing = 15
        )

     )
    
    layout = ft.Row(
        controls = [
            menu_lateral, 
            contenido
        ],
        expand = True
    )

    page.add(layout)

    mostrar_inicio()