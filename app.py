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

# ==========================================
# DESTETES
# ==========================================

from dao.destete_dao import DesteteDAO
from models.destete import Destete

def ver_destetes():
    try:    
        destete_dao = DesteteDAO()
        destetes = destete_dao.obtener_todos()

        print("=== Destetes en la base de datos ===")

        if len(destetes) == 0:
            print("No hay destetes registrados.")
        else:
            for destete in destetes:
                print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print(
                    f"ID: {destete.id}\nNúmero de Arete: {destete.arete}\n"
                    f"Fecha: {destete.fecha}\nNúmero de Lechones: {destete.numLechones}\n"
                    f"Peso Promedio: {destete.pesoPromedio}"
                )
                print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nConexion exitosa a la base de datos.")
    except Exception as e:
        print(f"Error: ")
        print(e)

def insertar_destete():
    arete = input("Escribe el número de arete de la cerda: ")
    fecha = input("Escribe la fecha de destete (AAAA/MM/DD): ")
    numLechones = input("Escribe el número de lechones: ")
    pesoPromedio = input("Escribe el peso promedio (kg): ")
    try:
        destete_dao = DesteteDAO()
        id = destete_dao.obtener_ultimo_id() + 1
        destete = Destete(id, arete, fecha, int(numLechones), float(pesoPromedio))
        destete_dao.insertar(destete)
        print("Insercion de destete realizada correctamente.")
    except Exception as e:
        print("Error al insertar un nuevo destete: ")
        print(e)

def actualizar_destete():
    print("Selecciona el destete a actualizar")
    try:
        destete_dao = DesteteDAO()
        ver_destetes()
        id = int(input("Escribe el id del destete a actualizar: "))
        arete = input("Escribe el nuevo número de arete: ")
        fecha = input("Escribe la nueva fecha (AAAA/MM/DD): ")
        numLechones = input("Escribe el nuevo número de lechones: ")
        pesoPromedio = input("Escribe el nuevo peso promedio (kg): ")
        
        destete = Destete(id, arete, fecha, int(numLechones), float(pesoPromedio))
        destete_dao.actualizar(destete)
        print(f'El destete con ID {id} ha sido actualizado correctamente')
    except Exception as e:
            print("Error al actualizar el destete")
            print(e)

def menu_destetes():
    print("1. Ver todos los destetes")
    print("2. Insertar un nuevo destete")
    print("3. Actualizar un destete")
    opcion = int(input("Selecciona una opcion (1-3): "))

    match opcion:
        case 1:
            ver_destetes()
        case 2:
            insertar_destete()
        case 3:
            actualizar_destete()
        

# ==========================================
# REPORTES
# ==========================================

from dao.destete_dao import DesteteDAO
# Si tienes algún reporteador o DAO de reportes, puedes importarlo aquí también
# from dao.reporte_dao import ReporteDAO 

def generar_reporte_destetes():
    try:
        destete_dao = DesteteDAO()
        destetes = destete_dao.obtener_todos()

        print("=== REPORTE GENERAL DE DESTETES ===")
        if len(destetes) == 0:
            print("No hay datos suficientes para generar el reporte.")
        else:
            total_lechones = 0
            peso_total = 0
            
            for destete in destetes:
                total_lechones += destete.numLechones
                peso_total += destete.pesoPromedio
                print(
                    f"ID: {destete.id} | Arete: {destete.arete} | "
                    f"Fecha: {destete.fecha} | Lechones: {destete.numLechones} | "
                    f"Peso Promedio: {destete.pesoPromedio} kg"
                )
            
            promedio_general = peso_total / len(destetes) if len(destetes) > 0 else 0
            print("--------------------------------------------------")
            print(f"Total de registros: {len(destetes)}")
            print(f"Suma total de lechones destetados: {total_lechones}")
            print(f"Promedio general de peso: {promedio_general:.2f} kg")
            
        print("\nReporte generado con éxito.")
    except Exception as e:
        print("Error al generar el reporte de destetes:")
        print(e)

def menu_reportes():
    print("=== MENÚ DE REPORTES ===" )
    print("1. Reporte general de destetes")
    print("2. Regresar")
    opcion = int(input("Selecciona una opción (1-2): "))

    match opcion:
        case 1:
            generar_reporte_destetes()
        case 2:
            print("Regresando...")
        case _:
            print("Opción no válida.")