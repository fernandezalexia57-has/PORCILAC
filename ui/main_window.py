import flet as ft

<<<<<<< Updated upstream
=======
from tkinter import dialog

>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
    #Reacciona al click del botón de cerdas en el menú lateral
    def mostrar_insertar_cerda(e=None):
        contenido.content = cerda_form(
        regresar_cerdas
    )
    page.update()

    def mostrar_lista_cerdas(e=None):

     contenido.content = cerda_list(
=======
    def mostrar_insertar_cerda(e=None):

            dialog = ft.AlertDialog(
                modal=True,
                content=cerda_form(
                lambda mensaje=None: cerrar_dialog_cerdas(dialog, mensaje)
                )
            )       

            page.overlay.append(dialog)
            dialog.open = True
            page.update()
        
    def mostrar_lista_cerdas(e=None):

        contenido.content = cerda_list(
>>>>>>> Stashed changes
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
    
<<<<<<< Updated upstream
=======
    
>>>>>>> Stashed changes
            if mensaje:
                page.show_dialog(
                ft.SnackBar(
                    content=ft.Text(mensaje),
                    bgcolor=ft.Colors.GREEN,
                )
            )
    
            page.update()

    page.update()
<<<<<<< Updated upstream

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
=======
    
    def cerrar_dialog_cerdas(dialog, mensaje=None):

        dialog.open = False
        page.update()

        regresar_cerdas(mensaje)


    def editar_cerda(cerda):

        dialog = ft.AlertDialog(
            modal=True,
                content=cerda_form(
                    lambda mensaje=None: cerrar_dialog_cerdas(dialog, mensaje),
                    cerda
                
            )
        )

        page.overlay.append(dialog)
        dialog.open = True
        page.update()
    

    
    


    def mostrar_insertar_parto(e=None):

        dialog = ft.AlertDialog(
            modal=True,
            content=parto_form(
            lambda mensaje=None: cerrar_dialog_partos(dialog, mensaje)
            )
        )       

        page.overlay.append(dialog)
        dialog.open = True
        page.update()
    
    def mostrar_lista_partos(e=None):

        contenido.content = parto_list(
        mostrar_insertar_parto,
        editar_parto
    )

    page.update()
            
    def regresar_partos(mensaje=None):
    
>>>>>>> Stashed changes
            contenido.content = parto_list(
            mostrar_insertar_parto,
            editar_parto
            )
    
<<<<<<< Updated upstream
=======
    
>>>>>>> Stashed changes
            if mensaje:
                page.show_dialog(
                ft.SnackBar(
                    content=ft.Text(mensaje),
                    bgcolor=ft.Colors.GREEN,
                )
            )
<<<<<<< Updated upstream
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
=======
    
            page.update()


    
    def cerrar_dialog_partos(dialog, mensaje=None):

        dialog.open = False
        page.update()

        regresar_partos(mensaje)
        

    def editar_parto(parto):

        dialog = ft.AlertDialog(
            modal=True,
                content=parto_form(
                    lambda mensaje=None: cerrar_dialog_partos(dialog, mensaje),
                    parto
                
            )
        )

        page.overlay.append(dialog)
        dialog.open = True
        page.update()
    
    
    
    def mostrar_insertar_servicio(e=None):
    
        dialog = ft.AlertDialog(
            modal=True,
            content=servicio_form(
            lambda mensaje=None: cerrar_dialog_servicios(dialog, mensaje)
            )
        )       

        page.overlay.append(dialog)
        dialog.open = True
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
    
    
    def cerrar_dialog_servicios(dialog, mensaje=None):

        dialog.open = False
        page.update()

        regresar_servicios(mensaje)
        
            
    def editar_servicio(servicio):
    
        dialog = ft.AlertDialog(
            modal=True,
                content=servicio_form(
                    lambda mensaje=None: cerrar_dialog_servicios(dialog, mensaje),
                    servicio
                
            )
        )

        page.overlay.append(dialog)
        dialog.open = True
        page.update()
    

    
    def mostrar_insertar_destete(e=None):
    
        dialog = ft.AlertDialog(
            modal=True,
            content=destete_form(
            lambda mensaje=None: cerrar_dialog(dialog, mensaje)
            )
        )       

        page.overlay.append(dialog)
        dialog.open = True
        page.update()
        
    def mostrar_lista_destetes(e=None):
    
            contenido.content = destete_list(
            mostrar_insertar_destete,
            editar_destete
    )
    
    page.update()
                
    def regresar_destetes(mensaje=None):
    
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
            page.update()
    
    def editar_destete(destete):
         contenido.content = destete_form(
            regresar_destetes,
            destete
    )
    page.update() 
=======
    
            page.update()
            
    
    def cerrar_dialog(dialog, mensaje=None):

        dialog.open = False
        page.update()

        regresar_destetes(mensaje)
    
    def editar_destete(destete):
    

        dialog = ft.AlertDialog(
            modal=True,
                content=destete_form(
                    lambda mensaje=None: cerrar_dialog(dialog, mensaje),
                    destete
                
            )
        )
        page.overlay.append(dialog)
        dialog.open = True
        page.update() 
>>>>>>> Stashed changes
    
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
<<<<<<< Updated upstream
        shape = ft.RoundedRectangleBorder(radius = 2),
=======
    shape = ft.RoundedRectangleBorder(radius = 2),
>>>>>>> Stashed changes
    ),
    on_click = lambda e:(seleccionar_boton(e.control), mostrar_insertar_cerda(e))
    )

    btn_empleados = ft.ElevatedButton(
    "Empleados",
    icon = ft.Icons.PEOPLE,
    width = 180,
    color = ft.Colors.BLACK,
    style = ft.ButtonStyle(
<<<<<<< Updated upstream
        shape = ft.RoundedRectangleBorder(radius = 2),
=======
    shape = ft.RoundedRectangleBorder(radius = 2),
>>>>>>> Stashed changes
    ),
    on_click = lambda e: (seleccionar_boton(e.control), mostrar_lista_usuarios(e))     
    )

    btn_cerdas = ft.ElevatedButton(
    "Cerdas",
    icon = ft.Icons.PIANO,
    width = 180,
    color = ft.Colors.BLACK,
    style = ft.ButtonStyle(
<<<<<<< Updated upstream
        shape = ft.RoundedRectangleBorder(radius = 2),
=======
    shape = ft.RoundedRectangleBorder(radius = 2),
>>>>>>> Stashed changes
    ),
    on_click = lambda e:(seleccionar_boton(e.control), mostrar_lista_cerdas(e))
    )

    btn_reproduccion = ft.ElevatedButton(
    "Reproducción",
    icon = ft.Icons.SWAP_HORIZ,
    width = 180,
    color = ft.Colors.BLACK,
    style = ft.ButtonStyle(
<<<<<<< Updated upstream
        shape = ft.RoundedRectangleBorder(radius = 2),
=======
    shape = ft.RoundedRectangleBorder(radius = 2),
>>>>>>> Stashed changes
    ),
    on_click = lambda e:(seleccionar_boton(e.control), mostrar_lista_servicios(e))
    )

    btn_partos = ft.ElevatedButton(
    "Partos",
    icon = ft.Icons.KEYBOARD_RETURN,
    width = 180,
    color = ft.Colors.BLACK,
    style = ft.ButtonStyle(
<<<<<<< Updated upstream
        shape = ft.RoundedRectangleBorder(radius = 2),
=======
    shape = ft.RoundedRectangleBorder(radius = 2),
>>>>>>> Stashed changes
    ),
    on_click = lambda e:(seleccionar_boton(e.control), mostrar_lista_partos(e))
    )

    btn_destete = ft.ElevatedButton(
    "Destete",
    icon = ft.Icons.CHILD_CARE,
    width = 180,
    color = ft.Colors.BLACK,
    style = ft.ButtonStyle(
<<<<<<< Updated upstream
        shape = ft.RoundedRectangleBorder(radius = 2),
=======
    shape = ft.RoundedRectangleBorder(radius = 2),
>>>>>>> Stashed changes
    ),
    on_click = lambda e:(seleccionar_boton(e.control), mostrar_lista_destetes(e))
    )

    btn_reportes = ft.ElevatedButton(
    "Reportes",
    icon = ft.Icons.INSIGHTS,
    width = 180,
    color = ft.Colors.BLACK,
    style = ft.ButtonStyle(
<<<<<<< Updated upstream
        shape = ft.RoundedRectangleBorder(radius = 2),
=======
    shape = ft.RoundedRectangleBorder(radius = 2),
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
                ft.Image(
                    src="logo.png",
                    width=240,
                    height=180,
                    fit="contain"
                ),
                ft.Container(height=15),
                ft.Column(
                    spacing=45,
=======
                ft.Column(
                    controls = [
                        ft.Text(
                            "Biblioteca",  
                            size = 22,
                            weight = ft.FontWeight.BOLD,
                            color = ft.Colors.WHITE
                        ),
                        ft.Text(
                            "Sistema de gestión",
                            size = 12,
                            color = ft.Colors.WHITE
                        ),
                        ft.Divider(color = ft.Colors.PINK_700),
                    ]
                ),
                ft.Column(
                    spacing=65,
>>>>>>> Stashed changes
                    controls=botones_menu
                ),
                ft.Column(
                    spacing = 65,
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                    controls = [ 
                    ]
                ),  
<<<<<<< Updated upstream
                ft.Container(expand=True),
                
=======
                ft.Container(expand=True)
>>>>>>> Stashed changes
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