import flet as ft

from dao.usuario_dao import UsuarioDAO
from ui.usuarios_form import usuario_form
from ui.usuarios_list import usuarios_list
from ui.cerda_form import cerda_form
from ui.cerda_list import cerda_list
from ui.cerda_detalles import cerda_detalles
from ui.servicio_form import servicio_form
from ui.servicio_list import servicio_list
from ui.parto_form import parto_form
from ui.parto_list import parto_list
from ui.destete_form import destete_form
from ui.destete_list import destete_list
from ui.reportes_form import reportes_form

def main_window(page: ft.Page):
    page.title = "Sistema de Gestion de Reproduccion de Cerdas"
    page.window_width = 1100
    page.window_height = 700
    page.padding = 0
    page.bgcolor = ft.Colors.WHITE

    contenido = ft.Container(padding=30, expand=True)

    botones_menu = []

    def seleccionar_boton(boton_activo):
        for btn in botones_menu:
            if btn == boton_activo:
                btn.height = 50
                btn.bgcolor = ft.Colors.WHITE
                btn.color = ft.Colors.PINK_600  
                btn.elevation = 4
            else:
                btn.height = 40
                btn.bgcolor = ft.Colors.PINK_300
                btn.color = ft.Colors.BLACK     
                btn.elevation = 0
        
        page.update()

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
    def cambiar_vista(funcion_vista, e):
        if e and e.control:
            seleccionar_boton(e.control)
        funcion_vista(e)

    def mostrar_inicio(e=None):
        contenido.content = inicio()
        page.update()
            
    #Reacciona al click del botón de usuarios en el menú lateral
    def mostrar_insertar_usuario(e=None):
        contenido.content = usuario_form(
            regresar=mostrar_lista_usuarios
        )
        page.update()

    def editar_usuario(usuario_seleccionado):
        print("¡Se hizo clic en editar!", usuario_seleccionado.nombre)
        # Llamamos al formulario PASANDO el usuario que vino de la fila
        contenido.content = usuario_form(
            regresar=mostrar_lista_usuarios,
            usuario=usuario_seleccionado
        )
        page.update()


    def eliminar_usuario(usuario_id):
        try:
            usuario_dao = UsuarioDAO()
            usuario_dao.eliminar(usuario_id)
            print(f"Usuario {usuario_id} eliminado exitosamente.")
            
            mostrar_lista_usuarios()
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")

    def mostrar_lista_usuarios(e=None):
        contenido.content = usuarios_list(
            nuevo_usuario=mostrar_insertar_usuario,
            editar_usuario=editar_usuario,
            eliminar_usuario=eliminar_usuario,
        )
        page.update()

    #Reacciona al click del botón de cerdas en el menú lateral
    def mostrar_insertar_cerda(e=None):
        contenido.content = cerda_form(
        regresar_cerdas
    )
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

    #Reacciona al click del botón de reproduccion en el menú lateral
    def mostrar_insertar_servicio(e=None):
            contenido.content = servicio_form(regresar_servicios)
            page.update()

    def mostrar_lista_servicios(e=None):
        if e: seleccionar_boton(e.control)
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

    #Reacciona al click del botón de partos en el menú lateral
    def mostrar_insertar_parto(e=None):
        contenido.content = parto_form(regresar_partos)
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
    
    #Reacciona al click del botón de destete en el menú lateral
    def mostrar_insertar_destete(e=None):
        contenido.content = destete_form(
         regresar_destetes
    )
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
    
    #Reacciona al click del botón de reportes en el menú lateral
    def mostrar_reportes(e=None):
        contenido.content = reportes_form(mostrar_inicio)
        page.update()



    btn_inicio = ft.ElevatedButton(
    "Inicio",
    icon = ft.Icons.HOME,
    width = 180,
    color = ft.Colors.BLACK,
    style = ft.ButtonStyle(
        shape = ft.RoundedRectangleBorder(radius = 2),
    ),
    on_click = lambda e:(seleccionar_boton(e.control), mostrar_insertar_cerda(e))
    )

    btn_empleados = ft.ElevatedButton(
    "Empleados",
    icon = ft.Icons.PEOPLE,
    width = 180,
    color = ft.Colors.BLACK,
    style = ft.ButtonStyle(
        shape = ft.RoundedRectangleBorder(radius = 2),
    ),
    on_click = lambda e: (seleccionar_boton(e.control), mostrar_lista_usuarios(e))     
    )

    btn_cerdas = ft.ElevatedButton(
    "Cerdas",
    icon = ft.Icons.PIANO,
    width = 180,
    color = ft.Colors.BLACK,
    style = ft.ButtonStyle(
        shape = ft.RoundedRectangleBorder(radius = 2),
    ),
    on_click = lambda e:(seleccionar_boton(e.control), mostrar_lista_cerdas(e))
    )

    btn_reproduccion = ft.ElevatedButton(
    "Reproducción",
    icon = ft.Icons.SWAP_HORIZ,
    width = 180,
    color = ft.Colors.BLACK,
    style = ft.ButtonStyle(
        shape = ft.RoundedRectangleBorder(radius = 2),
    ),
    on_click = lambda e:(seleccionar_boton(e.control), mostrar_lista_servicios(e))
    )

    btn_partos = ft.ElevatedButton(
    "Partos",
    icon = ft.Icons.KEYBOARD_RETURN,
    width = 180,
    color = ft.Colors.BLACK,
    style = ft.ButtonStyle(
        shape = ft.RoundedRectangleBorder(radius = 2),
    ),
    on_click = lambda e:(seleccionar_boton(e.control), mostrar_lista_partos(e))
    )

    btn_destete = ft.ElevatedButton(
    "Destete",
    icon = ft.Icons.CHILD_CARE,
    width = 180,
    color = ft.Colors.BLACK,
    style = ft.ButtonStyle(
        shape = ft.RoundedRectangleBorder(radius = 2),
    ),
    on_click = lambda e:(seleccionar_boton(e.control), mostrar_lista_destetes(e))
    )

    btn_reportes = ft.ElevatedButton(
    "Reportes",
    icon = ft.Icons.INSIGHTS,
    width = 180,
    color = ft.Colors.BLACK,
    style = ft.ButtonStyle(
        shape = ft.RoundedRectangleBorder(radius = 2),
    ),
    on_click = lambda e:(seleccionar_boton(e.control), mostrar_reportes(e))
    )

    botones_menu = [
    btn_inicio,
    btn_empleados,
    btn_cerdas,
    btn_reproduccion,
    btn_partos,
    btn_destete,
    btn_reportes
    ]


    menu_lateral = ft.Container(
        width = 240,
        bgcolor = ft.Colors.PINK_300,
        padding = 20,
        content = ft.Column(
            expand = True,
            controls = [
                ft.Image(
                    src="logo.png",
                    width=240,
                    height=180,
                    fit="contain"
                ),
                ft.Container(height=15),
                ft.Column(
                    spacing=45,
                    controls=botones_menu
                ),
                ft.Column(
                    spacing = 65,
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                    controls = [ 
                    ]
                ),  
                ft.Container(expand=True),
                
            ]
        )

     )
    
    layout = ft.Row(
            controls=[
                menu_lateral, 
                contenido
            ],
            expand=True,
            spacing=0
    )

    page.add(layout)
    
    seleccionar_boton(btn_inicio)

    mostrar_inicio()