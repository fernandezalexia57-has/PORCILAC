import flet as ft

from configparser import Error

from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario
from ui.main_window import main_window


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

def menu_usuarios():
    print("1. Ver todos los usuarios")
    print("2. Insertar un nuevo usuario")
    print("3. Actualizar un usuario")
    print("4. Eliminar un usuario")
    opcion = int(input("Seleciona una opcion (1-4): "))

    match opcion:
        case 1:
            ver_usuarios()
        case 2:
            insertar_usuarios()
        case 3:
            actualizar_usuarios()
        case 4:
            eliminar_usuarios()

ft.app(target = main_window)

# def main():
#     print("=== BIBLIOTECA UNIVERSITARIA ===")
#     print("Menu de opciones")
#     print("1.Menu de libros")
#     print("2.Menu de usuarios")
#     opcion = int(input("Selecciona una opcion (1-2): "))

#     match opcion:
#         case 1:
#             menu_libros()
#         case 2:
#             menu_usuarios()


#if __name__ == "__main__":
#     menu_usuarios()