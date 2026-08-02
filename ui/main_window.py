import flet as ft

from ui.destete_list import destete_list
from ui.parto_list import parto_list
from ui.servicio_list import servicio_list
from ui.cerda_from import cerda_form
from ui.cerda_list import cerda_list
from ui.parto_from import parto_form
from ui.servicio_from import servicio_form
from ui.destete_from import destete_form
from ui.cerda_detalles import cerda_detalles


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
    def editar_parto(parto):

     print(
        "Editando parto:",
        parto.id_parto
    )
    
    def mostrar_inicio(e=None):
        contenido.content = inicio()
        page.update()
            
  

    page.update()
    #Reacciona al click del botón de libros en el menú lateral
    def mostrar_insertar_cerda(e=None):

     contenido.content = cerda_form(
        regresar_cerdas
    )

    page.update()

    page.update()
    
    def mostrar_lista_cerdas(e=None):

     contenido.content = cerda_list(
        mostrar_insertar_cerda,
        editar_cerda,
        ver_detalles
        
    )

    page.update()
    
    def ver_detalles(cerda):

        contenido.content = cerda_detalles(
        cerda,
        regresar_cerdas
    )

    page.update()
            
    def regresar_cerdas(mensaje=None):
    
            contenido.content = cerda_list(
            mostrar_insertar_cerda,
            editar_cerda,
            ver_detalles
            )
    
            if mensaje:
                page.show_dialog(
                ft.SnackBar(
                    content=ft.Text(mensaje),
                    bgcolor=ft.Colors.GREEN,
                )
            )
    
            page.update()

    page.update()

    def editar_cerda(cerda):

     contenido.content = cerda_form(
        regresar_cerdas,
        cerda
    )

    page.update()
    

    page.update()

    page.update()
    


    def mostrar_insertar_parto(e=None):

     contenido.content = parto_form(
        regresar_partos
    )

    page.update()

    page.update()
    
    def mostrar_lista_partos(e=None):

     contenido.content = parto_list(
        mostrar_insertar_parto,
        editar_parto
    )

    page.update()
            
    def regresar_partos():

     contenido.content = parto_list(
        mostrar_insertar_parto,
        editar_parto
    )

    page.update()

    def editar_parto(parto):

     contenido.content = parto_form(
        regresar_partos,
        parto
    )

    page.update()
    

    page.update()

    page.update()
    
    
    def mostrar_insertar_servicio(e=None):
    
        contenido.content = servicio_form(
         regresar_servicios
        )
    
        page.update()
    
        page.update()
        
    def mostrar_lista_servicios(e=None):
    
         contenido.content = servicio_list(
            mostrar_insertar_servicio,
            editar_servicio
        )
    
         page.update()
                
    def regresar_servicios(mensaje=None):

        contenido.content = servicio_list(
        mostrar_insertar_servicio,
        editar_servicio
        )

        if mensaje:
            page.show_dialog(
            ft.SnackBar(
                content=ft.Text(mensaje),
                bgcolor=ft.Colors.GREEN,
            )
        )

        page.update()
    
    def editar_servicio(servicio):
    
         contenido.content = servicio_form(
            regresar_servicios,
            servicio
    )
    
    page.update() 
    
    
    def mostrar_insertar_parto(e=None):

     contenido.content = parto_form(
        regresar_partos
    )

    page.update()

    page.update()
    
    def mostrar_lista_partos(e=None):

     contenido.content = parto_list(
        mostrar_insertar_parto,
        editar_parto
    )

    page.update()
            
    def regresar_partos(mensaje=None):
    
            contenido.content = parto_list(
            mostrar_insertar_parto,
            editar_parto
            )
    
            if mensaje:
                page.show_dialog(
                ft.SnackBar(
                    content=ft.Text(mensaje),
                    bgcolor=ft.Colors.GREEN,
                )
            )
    
            page.update()

    def editar_parto(parto):

     contenido.content = parto_form(
        regresar_partos,
        parto
    )

    page.update()
    

    page.update()

    page.update()
    
    
    def mostrar_insertar_destete(e=None):
    
        contenido.content = destete_form(
         regresar_destetes
    )
    
    page.update()
    
    page.update()
        
    def mostrar_lista_destetes(e=None):
    
         contenido.content = destete_list(
            mostrar_insertar_destete,
            editar_destete
    )
    
    page.update()
                
    def regresar_destetes(mensaje=None):
    
            contenido.content = destete_list(
            mostrar_insertar_destete,
            editar_destete
            )
    
            if mensaje:
                page.show_dialog(
                ft.SnackBar(
                    content=ft.Text(mensaje),
                    bgcolor=ft.Colors.GREEN,
                )
            )
    
            page.update()
    
    def editar_destete(destete):
    
         contenido.content = destete_form(
            regresar_destetes,
            destete
    )
    
    page.update() 
    
    
    

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
                    on_click = mostrar_lista_cerdas
                ),
                ft.ElevatedButton(
                    "Reproducción",
                    icon = ft.Icons.SWAP_HORIZ,
                    width = 180,
                    color = ft.Colors.BLACK,
                    style = ft.ButtonStyle(
                        shape = ft.RoundedRectangleBorder(radius = 2),
                    ),
                     on_click = mostrar_lista_servicios
                   
                ),
                ft.ElevatedButton(
                    "Partos",
                    icon = ft.Icons.KEYBOARD_RETURN,
                    width = 180,
                    color = ft.Colors.BLACK,
                    style = ft.ButtonStyle(
                        shape = ft.RoundedRectangleBorder(radius = 2),
                    ),
                    on_click = mostrar_lista_partos
                ),
                ft.ElevatedButton(
                    "Destete",
                    icon = ft.Icons.CHILD_CARE,
                    width = 180,
                    color = ft.Colors.BLACK,
                    style = ft.ButtonStyle(
                        shape = ft.RoundedRectangleBorder(radius = 2),
                    ),
                    on_click = mostrar_lista_destetes
                 
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