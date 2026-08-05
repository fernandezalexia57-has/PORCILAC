import flet as ft

from ui.usuarios_form import usuario_form
from ui.usuarios_list import usuarios_list
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario

def empleado_view(page: ft.Page):
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
            
    menu_lateral = ft.Container(
        width = 220,
        bgcolor = ft.Colors.PINK_300,
        padding = 20,
        content = ft.Column(
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
                    on_click = mostrar_insertar_usuario
                ),
                ft.ElevatedButton(
                    "Reprodcción",
                    icon = ft.Icons.SWAP_HORIZ,
                    width = 180,
                    color = ft.Colors.BLACK,
                    style = ft.ButtonStyle(
                        shape = ft.RoundedRectangleBorder(radius = 2),
                    ),
                    on_click = mostrar_insertar_usuario
                ),
                ft.ElevatedButton(
                    "Partos",
                    icon = ft.Icons.KEYBOARD_RETURN,
                    width = 180,
                    color = ft.Colors.BLACK,
                    style = ft.ButtonStyle(
                        shape = ft.RoundedRectangleBorder(radius = 2),
                    ),
                    on_click = mostrar_insertar_usuario
                ),
                ft.ElevatedButton(
                    "Destete",
                    icon = ft.Icons.CHILD_CARE,
                    width = 180,
                    color = ft.Colors.BLACK,
                    style = ft.ButtonStyle(
                        shape = ft.RoundedRectangleBorder(radius = 2),
                    ),
                    on_click = mostrar_insertar_usuario
                ),
                ft.ElevatedButton(
                    "Reportes",
                    icon = ft.Icons.INSIGHTS,
                    width = 180,
                    color = ft.Colors.BLACK,
                    style = ft.ButtonStyle(
                        shape = ft.RoundedRectangleBorder(radius = 2),
                    ),
                    on_click = mostrar_insertar_usuario
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

    page.update()