import flet as ft 

from models.cerda import Cerda
from dao.cerda_dao import CerdaDAO 

def cerda_form(regresar):
    arete_imput = ft.TextField(
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
        ft.dropdown.Option("Lactancia"),
        ft.dropdown.Option("Vacía")
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
    
    mensaje = ft.Text(
        "",
        color = ft.Colors.GREEN
    )
    
    def guardar_cerda(e):
        #Recuperar los valores del TextField
        arete = arete_imput.value #nombre del TextField. value
        raza = raza_input.value
        color = color_input.value
        edad = edad_input.value
        estado = estado_input.value 
        fecha = fecha_input.value 
         
        #Validacion de campos vacios
        if arete == "" or raza == "" or color == "" or edad == "" or estado == "" or fecha == "":
            mensaje.value = "Todos los campos son obligatorios"
            mensaje.color = ft.Colors.RED
            e.page.update()
            return 
        
        try:
            cerda_dao = CerdaDAO()
            id = cerda_dao.obtener_ultimo_id() +1 
            
            nueva_cerda = Cerda(
                id=id,
                arete= arete,
                raza= raza,
                color= color,
                edad=int(edad),
                estado=estado,
                fecha=fecha
            )
            
            cerda_dao.insertar(nueva_cerda)
            
            mensaje.value = f"La cerda  '{arete}' ha sido insertada"
            mensaje.color = ft.Colors.GREEN
            arete_imput.value = ""
            raza_input.value = ""
            color_input.value = ""
            edad_input.value = ""
            estado_input.value = ""
            fecha_input.value = ""
            
            
        except ValueError:
            mensaje.value = "El campo 'Edad' debe ser un número entero"
            mensaje.color = ft.Colors.RED
        except Exception as error:
            mensaje.value = f"Error al insertar la cerda: {error}"
            mensaje.color=ft.Colors.RED
            
            
        e.page.update()
            
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
               
               arete_imput,
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
                 "Registrar cerda",
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