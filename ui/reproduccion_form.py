import flet as ft

from models.reproduccion import Reproduccion
from dao.reproduccion_dao import ReproduccionDAO

def reproduccion_form(regresar):
    num_arete_input = ft.TextField(
        label="Número de arete de la cerda: ",
        width = 400
    )

    fecha_reproduccion_input = ft.TextField(
        label="Fecha de monta: ",
        width = 400
    )

    tipo_input = ft.Dropdown(
    label="Tipo de reproducción",
    width=400,
    options=[
        ft.dropdown.Option("1", "Monta natural"),
        ft.dropdown.Option("2", "Inseminación artificial"),
    ],
    value="1",  # Opción seleccionada por defecto
    )

    mensaje = ft.Text(
        "",
        color = ft.Colors.GREEN
    )

    def guardar_reproduccion(e):
        #Recupera los valores de TexField
        num_arete = num_arete_input.value
        fecha_reproduccion = fecha_reproduccion_input.value
        tipo = tipo_input.value

        #Validación de campos vacíos
        if num_arete == "" or fecha_reproduccion == "" or tipo == "":
            mensaje.value = "Todos los campos son obligatorios"
            mensaje.color = ft.Colors.RED
            e.page.update()
            return
        
        try: 
            reproduccion_dao = ReproduccionDAO()
            id = reproduccion_dao.obtener_ultimo_id() + 1
            
            nueva_reproduccion = Reproduccion(
                id=id,
                numArete=num_arete,
                fecha_reproduccion=fecha_reproduccion,
                tipo=tipo
            )

            reproduccion_dao.insertar(nueva_reproduccion)

            mensaje.value = f"Reproducción '{num_arete}' ha sido insertada"
            print(f"Número de Arete: '{num_arete}', Fecha: '{fecha_reproduccion}', Tipo: '{tipo}'")
            mensaje.color = ft.Colors.GREEN
            num_arete_input.value = ""
            fecha_reproduccion_input.value = ""
            tipo_input.value = None

        except ValueError:
            mensaje.value = "El campo 'Número de Arete' debe ser un número entero"
            mensaje.color = ft.Colors.RED
        except Exception as error:
            mensaje.value = f"Error al insertar la reproducción: {error}"
            mensaje.color = ft.Colors.RED
            

            e.page.update()    


    return ft.Container(
        padding = 30,
        content = ft.Column(
            controls = [
                ft.Text(
                    "Registrar nueva reproducción", 
                    size = 24,
                    weight = ft.FontWeight.BOLD
                ),

                ft.Text(
                    "Captura los datos básicos de la reproducción",
                    size = 14,
                    color = ft.Colors.BLUE_GREY_600
                ),

                num_arete_input,
                fecha_reproduccion_input,
                tipo_input,

                ft.Row(
                    controls = [
                        ft.ElevatedButton(
                            "Cancelar",
                            icon=ft.Icons.CANCEL,
                            style=ft.ButtonStyle(
                            color=ft.Colors.BLACK,
                            side=ft.BorderSide(1, ft.Colors.BLACK)
                            ),
                            on_click = lambda e: regresar()
                        ),
                        ft.OutlinedButton(
                            "Registrar monta",
                            icon=ft.Icons.ADD,
                            style=ft.ButtonStyle(
                            bgcolor="#E85A8E",
                            color=ft.Colors.WHITE
                            ),
                            on_click = guardar_reproduccion
                        )
                    ]
                ), 
                mensaje 
            ],
            spacing = 15 
        )
    )