import flet as ft 
from ui.main_window import main_window
from dao.cerda_dao import CerdaDAO
from models.cerda import Cerda

def ver_cerda(): 
    try:
        cerda_dao = CerdaDAO()
        
        cerdas = cerda_dao.obtener_todos()
        
        print("=== Cerdas en la granja ===")
        
        if len(cerdas) ==0:
            print("No hay cerdas registradas.")
        else:
            for cerda in cerdas:
                print(
                    f"ID: {cerda.id}, Num. Arete: {cerda.arete}, "
                    f"Raza: {cerda.raza}, Color: {cerda.color}, Edad: {cerda.edad}, "
                    f"Estado: {cerda.estado }, Fecha de registro: {cerda.fecha } "
                )
                print("-------------------------------------------------------------------------------")
        print("\n conexion exitosa a la base de datos")
    except Exception as e:
        print("Error: ")
        print(e)
        
def insertar_cerda():
    arete = input("Escribe el numero de arete de la cerda: ")
    raza = input("Escribe la raza de la cerda: ")
    color = input("Escribe el color de la cerda: ")
    edad = int(input("Escribe la edad de la cerda: "))
    estado = input("Escribe el estado de la cerda: ")
    fecha = input("Escribe fecha en la que se registro de la cerda: ")
    

    try:
        cerda_dao = CerdaDAO()

        nuevo_id = cerda_dao.obtener_ultimo_id() + 1

        cerda = Cerda(
            None,
            arete,
            raza,
            color,
            edad,
            estado,
            fecha
        )

        cerda_dao.insertar(cerda)

        print("Inserción realizada con éxito")

    except Exception as e:
        print("Error al insertar una nueva cerda")
        print(e)
        
        
def actualizar_cerda():
    try:
        cerda_dao = CerdaDAO()

        print("Lista de cerdas")
        ver_cerda()

        id = int(input("Seleccione el id de la cerda a actualizar: "))

        arete = input("Escribe el nuevo arete de la cerda: ")
        raza = input("Escribe la nueva raza de la cerda: ")
        color = input("Escribe el nuevo color de la cerda: ")
        edad = int(input("Escribe la nueva edad de la cerda: "))
        estado = input("Escribe el nuevo estado reproductivo de la cerda: ")
        fecha = input("Escribe la nueva fecha en la que se registro de la cerda: ")
        

        cerda = Cerda(
            id,
            arete,
            raza,
            color,
            edad,
            estado,
            fecha
        )

        cerda_dao.actualizar(cerda)

        print(f"La cerda {id} fue actualizada con éxito")

    except Exception as e:
        print("Error al actualizar la cerda")
        print(e)
        
def eliminar_cerda():
   
    try:
        cerda_dao = CerdaDAO()
        
        print("Lista de cerdas")
        ver_cerda()

        id = int(input("Escriba el id de la cerda a eliminar: "))
        cerda_dao.eliminar(id)

        print(f"La cerda {id} ha sido eliminada con exito")

    except Exception as e:
        print(f"Error al eliminar la cerda {id}")   
        print(e)
    
def main():
    print ("=== GRANJA ===")
    print("Menú de opciones")
    print("1. Ver todas las cerdas")
    print("2. Insertar una nueva cerda")
    print("3. Actualizar el registro de una cerda")
    print("4. Eliminar el registro de una cerda")
    opcion = int(input("Seleccciona una opción (1-4):"))
    
    match opcion:
        case 1:
            ver_cerda()
        case 2:
            insertar_cerda()
        case 3:
            actualizar_cerda()
        case 4:
            eliminar_cerda()
            
ft.app(target = main_window)
    

if __name__ == "__main__":
     main()          