import flet as ft

from configparser import Error

from ui.login_inicio import login_view
<<<<<<< Updated upstream
from dao.usuario_dao import UsuarioDAO
from ui.cerda_detalles import cerda_detalles
from dao.servicio_dao import ServicioDAO
from dao.reproduccion_dao import ReproduccionDAO
from models.usuario import Usuario
from models.reproduccion import Reproduccion
from ui.main_window import main_window
from ui.empleado_view import empleado_view
=======
from ui.main_window import main_window
from ui.empleado_view import empleado_view
from ui.restablecer_form import restablecer_form
from dao.usuario_dao import UsuarioDAO
from ui.cerda_detalles import cerda_detalles
from dao.servicio_dao import ServicioDAO
from dao.reproduccion_dao import ReproduccionDAO
from models.usuario import Usuario
from models.reproduccion import Reproduccion

>>>>>>> Stashed changes

sesion_usuario = {}  # Diccionario para almacenar la sesión del usuario

def main(page: ft.Page):
<<<<<<< Updated upstream
    # Función de relleno por si hace clic en ingresar
    # def ir_a_main(datos=None):
    #     page.controls.clear()
    #     main_window(page)
    #     page.update()
    login_view(page)

    def route_change(route):
        page.views.clear()  # Limpiamos las vistas anteriores por completo
        rol = str(sesion_usuario.get("rol", "")).strip().lower()

        if page.route == "/" or page.route == "/login":
            page.views.append(
                ft.View(
                    route="/login",
                    controls=[],  # El contenido lo pinta login_view
                    padding=0
                )
            )
            # Llamamos a tu función de login pasándole la página
            login_view(page, sesion_usuario)

        elif page.route == "/main_window":
            if "administrador" in rol or "admin" in rol:
                page.views.append(
                    ft.View(
                        route="/main_window",
                        controls=[],
                        padding=0
                    )
                )
                main_window(page)
            else:
                page.go("/login")

        elif page.route == "/empleado":
            if "empleado" in rol:
                page.views.append(
                    ft.View(
                        route="/empleado",
                        controls=[],
                        padding=0
                    )
                )
                empleado_view(page)
            else:
                page.go("/login")

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Arrancamos en el login
=======

    def route_change(e):
            # Limpiamos los controles anteriores antes de cargar la vista elegida
            page.clean()
            rol = str(sesion_usuario.get("rol", "")).strip().lower()

            if page.route == "/" or page.route == "/login":
                login_view(page, sesion_usuario)

            elif page.route == "/restablecer":
                restablecer_form(page)

            elif page.route == "/main_window":
                if "administrador" in rol or "admin" in rol:
                    main_window(page)
                else:
                    page.go("/login")

            elif page.route == "/empleado":
                if "empleado" in rol:
                    empleado_view(page)
                else:
                    page.go("/login")
            else:
                # Ruta no encontrada: regresa al login
                page.go("/login")

            page.update()

    page.on_route_change = route_change
>>>>>>> Stashed changes
    page.go("/login")

if __name__ == "__main__":
    ft.app(target=main)



#USUARIOS

def ver_usuarios():
    try:    
        usuario_dao = UsuarioDAO()

        usuarios = usuario_dao.obtener_todos()

        print("=== Usuarios en la base de datos ===")

        if len(usuarios) == 0:
            print("No hay usuarios registrados.")
        else:
            for usuario in usuarios:
                print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print(
                    f"ID: {usuario.id}\nNombre: {usuario.nombre}\n"
                    f"Apellido Paterno: {usuario.apellidoPaterno}\nApellido Materno: {usuario.apellidoMaterno}\n"
                    f"Numero de Empleado: {usuario.noEmpleado}\nTipo: {usuario.tipo}\n"
                    f"Correo: {usuario.correo}\nContraseña: {usuario.password}"
                )
                print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nConexion exitosa a la base de datos.")
    except Exception as e:
        print(f"Error: ")
        print(e)

def insertar_usuarios():
    nombre = input("Escribe el nombre del nuevo usuario: ")
    apellidoPaterno = input("Escribe el apellido paterno del nuevo usuario: ")
    apellidoMaterno = input("Escribe el apellido materno del nuevo usuario: ")
    noEmpleado = input("Escribe el numero de empleado del usuario nuevo: ")
    tipo = input("Escribe el tipo de empleado del nuevo usuario: ")
    correo = input("Escribe el correo del nuevo usuario: ")
    password = input("Escribe la contraseña del nuevo usuario: ")
    try:
        usuario_dao = UsuarioDAO()
        id = usuario_dao.obtener_ultimo_id() + 1
        usuario = Usuario(id, nombre, apellidoPaterno, apellidoMaterno, noEmpleado, tipo, correo, password)
        usuario_dao.insertar(usuario)
        print("Insercion realizada correctamente.")
    except Exception as e:
        print("Error al insertar un nuevo usuario: ")
        print(e)

def actualizar_usuarios():
    print("Selecciona el usuario a actualizar")
    try:
        usuario_dao = UsuarioDAO()
        ver_usuarios()
        id = int(input("Escribe el id del usuario a actualizar: "))
        nombre = input("Escribe el nuevo nombre del usuario: ")
        apellidoPaterno = input("Escribe el nuevo apellido paterno del usuario: ")
        apellidoMaterno = input("Escribe el nuevo apellido materno del usuario: ")
        noEmpleado = input("Escribe el nuevo numero de empleado del usuario: ")
        tipo = input("Escribe el nuevo tipo de empleado del usuario: ")
        correo = input("Escribe el nuevo correo del usuario: ")
        password = input("Escribe la nueva contraseña del usuario: ")
        usuario = Usuario(id, nombre, apellidoPaterno, apellidoMaterno, noEmpleado, tipo, correo, password)
        usuario_dao.actualizar(usuario)
        print(f'El usuario con ID {id} ha sido actualizado correctamente')
    except Exception as e:
            print("Error al actualizar un usuario")
            print(e)

def eliminar_usuarios():
    try:
        usuario_dao = UsuarioDAO()
        print("Lista de usuarios disponibles:")
        ver_usuarios()
        id = int(input("Escribe el id del usuario a eliminar: "))
        usuario_dao.eliminar(id)
        print(f"El usuario {id} ha sido eliminado con exito")
    except Exception as e:
        print(f"Error al eliminar el usuario {id}")
        print(e)

<<<<<<< Updated upstream
#REPRODUCCION

def ver_reproduccion():
    try:    
        reproduccion_dao = ReproduccionDAO()

        reproducciones = reproduccion_dao.obtener_todos()

        print("=== Reproducción en la base de datos ===")

        if len(reproducciones) == 0:
            print("No hay registros de reproducción.")
=======
>>>>>>> Stashed changes

        else:
            for rep in reproducciones:
                print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print(
                    f"ID: {rep.id}\nNumero de Arete: {rep.numArete}\nFecha: {rep.fecha_reproduccion}\nTipo: {rep.tipo}"
                )
                print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nConexion exitosa a la base de datos.")
    except Exception as e:
        print(f"Error: ")
        print(e)

<<<<<<< Updated upstream
=======

#REPRODUCCION

def ver_reproduccion():
    try:    
        reproduccion_dao = ReproduccionDAO()

        reproducciones = reproduccion_dao.obtener_todos()

        print("=== Reproducción en la base de datos ===")

        if len(reproducciones) == 0:
            print("No hay registros de reproducción.")

        else:
            for rep in reproducciones:
                print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print(
                    f"ID: {rep.id}\nNumero de Arete: {rep.numArete}\nFecha: {rep.fecha_reproduccion}\nTipo: {rep.tipo}"
                )
                print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nConexion exitosa a la base de datos.")
    except Exception as e:
        print(f"Error: ")
        print(e)

>>>>>>> Stashed changes
def insertar_reproduccion():
    numArete = input("Escribe el número de arete de la nueva reproducción: ")
    fecha = input("Escribe la fecha de la nueva reproducción: ")
    tipo = input("Escribe el tipo de la nueva reproducción: ")
    try:
        reproduccion_dao = ReproduccionDAO()
        id = reproduccion_dao.obtener_ultimo_id() + 1
        reproduccion = Reproduccion(id, numArete, fecha, tipo)
        reproduccion_dao.insertar(reproduccion)
        print("Insercion realizada correctamente.")
    except Exception as e:
        print("Error al insertar una nueva reproducción: ")
        print(e)

def actualizar_reproduccion():
    print("Selecciona la reproducción a actualizar")
    try:
        reproduccion_dao = ReproduccionDAO()
        ver_reproduccion()
        id = int(input("Escribe el id de la reproducción a actualizar: "))
        numArete = input("Escribe el nuevo número de arete de la reproducción: ")
        fecha = input("Escribe la nueva fecha de la reproducción: ")
        tipo = input("Escribe el nuevo tipo de la reproducción: ")
        reproduccion = Reproduccion(id, numArete, fecha, tipo)
        reproduccion_dao.actualizar(reproduccion)
        print(f'La reproducción con ID {id} ha sido actualizada correctamente')
    except Exception as e:
            print("Error al actualizar una reproducción")
            print(e)

def eliminar_reproduccion():
    try:
        reproduccion_dao = ReproduccionDAO()
        print("Lista de reproducciones disponibles:")
        ver_reproduccion()
        id = int(input("Escribe el id de la reproducción a eliminar: "))
        reproduccion_dao.eliminar(id)
        print(f"La reproducción {id} ha sido eliminada con exito")
    except Exception as e:
        print(f"Error al eliminar la reproducción {id}")
        print(e)