import flet as ft 

from models.cerda import Cerda
from dao.cerda_dao import CerdaDAO 

def cerda_form(regresar, cerda=None):
    arete_input = ft.TextField(
        label ="Número de Arete de la cerda: ",
        hint_text="001",
        width= 400
    )

    
    raza_input = ft.Dropdown(
     label="Raza",
     width=400,
     options=[
        ft.dropdown.Option("Yorkshire"),
        ft.dropdown.Option("Landrace"),
        ft.dropdown.Option("Duroc"),
        ft.dropdown.Option("Pietrain"),
        ft.dropdown.Option("Hampshire")
     ]
    )
    
    color_input = ft.Dropdown(
     label="Color",
     width=400,
     options=[
        ft.dropdown.Option("Blanco"),
        ft.dropdown.Option("Negro"),
        ft.dropdown.Option("Rojo"),
        ft.dropdown.Option("Manchado")
     ]
     )
    
    edad_input = ft.TextField(
     label="Edad",
     value="1",
     width=300,
     read_only=True,
     text_align=ft.TextAlign.CENTER
     )

    def aumentar(e):
     edad_input.value = str(int(edad_input.value) + 1)
     e.page.update()

    def disminuir(e):
     edad = int(edad_input.value)
     if edad > 1:
        edad_input.value = str(edad - 1)
        e.page.update()

    edad_row = ft.Row(
     controls=[
        edad_input,
        ft.IconButton(
            icon=ft.Icons.REMOVE,
            tooltip="Disminuir edad",
            on_click=disminuir
        ),
        ft.IconButton(
            icon=ft.Icons.ADD,
            icon_color=ft.Colors.GREEN,
            tooltip="Aumentar edad",
            on_click=aumentar
        ),
     ]
     )

    estado_input = ft.Dropdown(
     label="Estado reproductivo",
     width=400,
     options=[
        ft.dropdown.Option("Celo"),
        ft.dropdown.Option("Gestante"),
        ft.dropdown.Option("Lactante"),
        ft.dropdown.Option("Vacía"),
        ft.dropdown.Option("Baja")
     ]
    )
    
    fecha_input = ft.TextField(
     label="Fecha de registro",
      hint_text="AAAA/MM/DD",
     width=340,
     read_only=True
     )

    def seleccionar_fecha(e):
     if e.control.value:
        fecha_input.value = e.control.value.strftime("%Y/%m/%d")
        e.page.update()

    date_picker = ft.DatePicker(
    on_change=seleccionar_fecha
    )

    fecha_row = ft.Row(
     controls=[
        fecha_input,
        ft.IconButton(
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: e.page.show_dialog(date_picker)
        )
     ]
     )

    # ==========================
    # CARGAR DATOS PARA EDITAR
    # ==========================

    if cerda:

        arete_input.value = str(
            cerda.arete
        )
        
        raza_input.value = str(
            cerda.raza
        )
        
        color_input.value = str(
            cerda.color
        )
        
        edad_input.value = str(
            cerda.edad
        )
        
        estado_input.value = str(
            cerda.estado
        )
        

        fecha_input.value = str(
            cerda.fecha
        )


    mensaje = ft.Text(
        "",
    color = ft.Colors.GREEN
    )

    # Guardar/ Actualizar
    def guardar_cerda(e):
        #Recuperar los valores del TextField
        arete = arete_input.value #nombre del TextField. value
        raza = raza_input.value
        color = color_input.value
        edad = edad_input.value
        estado = estado_input.value 
        fecha = fecha_input.value 
         
        #Validacion de campos vacios
        if not arete_input.value:
            mensaje.value = "Escriba el número de arete de la cerda"
            mensaje.color = ft.Colors.RED
            e.page.update()
            return 

        
        if len(arete_input.value) != 3 or not arete_input.value.isdigit():
            mensaje.value = "El número de arete debe contener exactamente 3 dígitos"
            mensaje.color = ft.Colors.RED
            e.page.update()
            return


        if not raza_input.value:


            mensaje.value = (
                "Seleccione la raza de la cerda"
            )

            mensaje.color = ft.Colors.RED

            e.page.update()

            return
        
        if not color_input.value:


            mensaje.value = (
                "Seleccione el color de la cerda"
            )

            mensaje.color = ft.Colors.RED

            e.page.update()

            return
        
        if not estado_input.value:


            mensaje.value = (
                "Seleccione el estado reproductivo en el que se encuentra de la cerda"
            )

            mensaje.color = ft.Colors.RED

            e.page.update()

            return
        
        
        if not fecha_input.value:


            mensaje.value = (
                "Seleccione la fecha de registro"
            )

            mensaje.color = ft.Colors.RED

            e.page.update()

            return
        
        
        cerda_dao = CerdaDAO()
        
        
        if not cerda:
            if cerda_dao.existe_arete(arete):
                mensaje.value = (
                f"Ya existe una cerda con el arete {arete}"
                 )
                mensaje.color = ft.Colors.RED
                e.page.update()
                return

        # ==========================
        # EDITAR
        # ==========================

        if cerda:


            cerda.arete = arete

            
            cerda.raza = raza_input.value
            
            cerda.color = color_input.value

            cerda.edad = int(
                edad_input.value
                )


            cerda.estado = estado_input.value


            cerda.fecha = fecha_input.value
            

            cerda_dao.actualizar(
             cerda
                )


            regresar(
             f"Cerda {cerda.arete} actualizada correctamente"
            )
            
            



        # ==========================
        # NUEVO
        # ==========================

        else:


            nuevo_cerda = Cerda(
            None,
            arete_input.value,
            raza_input.value,
            color_input.value,
            int(edad_input.value),
            estado_input.value,
            fecha_input.value
            )

            cerda_dao.insertar(nuevo_cerda)

            regresar("Cerda registrada correctamente")

            
    return ft.Container(
       padding = 30,
       content = ft.Column(
           controls = [
               ft.Text(
                   "Registro de nueva cerda",
                   size = 24,
                   weight= ft.FontWeight.BOLD
               ),
               
               ft.Text(
                   "Capture los datos básicos de la cerda",
                   size = 14,
                   color = ft.Colors.BLACK_87
               ),
               
               arete_input,
               raza_input,
               color_input,
               edad_row,
               estado_input,
               fecha_row,
               date_picker,
               
               
               ft.Row(  
                    controls = [
                        ft.OutlinedButton(
                            "Cancelar",
                            icon=ft.Icons.CANCEL,
                            style=ft.ButtonStyle(
                            color=ft.Colors.BLACK,
                            side=ft.BorderSide(1, ft.Colors.BLACK)
                            ),
                            on_click=lambda e: regresar()
                        ),
                        ft.ElevatedButton(
                            "Actualizar cerda" if cerda else "Registrar cerda",
                            icon=ft.Icons.ADD,
                            style=ft.ButtonStyle(
                            bgcolor="#E85A8E",
                            color=ft.Colors.WHITE
                            ),
                            on_click=guardar_cerda
                        )
                    ],
                ),
               mensaje
           ],
           spacing= 15
       )
   ) 