import flet as ft 

from models.destete import Destete
from dao.destete_dao import DesteteDAO

def destete_form(regresar):
    arete_imput = ft.TextField(
        label="Número de Arete de la cerda:",
        hint_text="001",
        width=400
    )
    
    fecha_input = ft.TextField(
        label="Fecha de destete",
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

    lechones_input = ft.TextField(
        label="Número de lechones",
        value="1",
        width=300,
        read_only=True,
        text_align=ft.TextAlign.CENTER
    )

    def aumentar_lechones(e):
        lechones_input.value = str(int(lechones_input.value) + 1)
        e.page.update()

    def disminuir_lechones(e):
        lechones = int(lechones_input.value)
        if lechones > 1:
            lechones_input.value = str(lechones - 1)
            e.page.update()

    lechones_row = ft.Row(
        controls=[
            lechones_input,
            ft.IconButton(
                icon=ft.Icons.REMOVE,
                tooltip="Disminuir lechones",
                on_click=disminuir_lechones
            ),
            ft.IconButton(
                icon=ft.Icons.ADD,
                icon_color=ft.Colors.GREEN,
                tooltip="Aumentar lechones",
                on_click=aumentar_lechones
            ),
        ]
    )

    peso_input = ft.TextField(
        label="Peso promedio (kg)",
        hint_text="10.5",
        width=400
    )
    
    mensaje = ft.Text(
        "",
        color=ft.Colors.GREEN
    )
    
    def guardar_destete(e):
        arete = arete_imput.value
        fecha = fecha_input.value
        lechones = lechones_input.value
        peso = peso_input.value
         
        if arete == "" or fecha == "" or lechones == "" or peso == "":
            mensaje.value = "Todos los campos son obligatorios"
            mensaje.color = ft.Colors.RED
            e.page.update()
            return 
        
        try:
            destete_dao = DesteteDAO()
            id = destete_dao.obtener_ultimo_id() + 1 
            
            nuevo_destete = Destete(
                id=id,
                arete=arete,
                fecha=fecha,
                numLechones=int(lechones),
                pesoPromedio=float(peso)
            )
            
            destete_dao.insertar(nuevo_destete)
            
            mensaje.value = f"El destete de la cerda '{arete}' ha sido insertado"
            mensaje.color = ft.Colors.GREEN
            arete_imput.value = ""
            fecha_input.value = ""
            lechones_input.value = "1"
            peso_input.value = ""
            
        except ValueError:
            mensaje.value = "Los campos numéricos deben tener valores válidos"
            mensaje.color = ft.Colors.RED
        except Exception as error:
            mensaje.value = f"Error al insertar el destete: {error}"
            mensaje.color = ft.Colors.RED
            
        e.page.update()
            
    return ft.Container(
        padding=30,
        content=ft.Column(
            controls=[
                ft.Text(
                    "Registro de nuevo destete",
                    size=24,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Text(
                    "Capture los datos del destete",
                    size=14,
                    color=ft.Colors.BLACK_87
                ),
                arete_imput,
                fecha_row,
                date_picker,
                lechones_row,
                peso_input,
                ft.Row(  
                    controls=[
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
                            "Registrar destete",
                            icon=ft.Icons.ADD,
                            style=ft.ButtonStyle(
                                bgcolor="#E85A8E",
                                color=ft.Colors.WHITE
                            ),
                            on_click=guardar_destete
                        )
                    ],
                ),
                mensaje
            ],
            spacing=15
        )
    )