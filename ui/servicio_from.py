import flet as ft


from models.servicio import Servicio
from dao.servicio_dao import ServicioDAO
from dao.cerda_dao import CerdaDAO
from dao.destete_dao import DesteteDAO
from datetime import datetime, timedelta

def servicio_form(regresar, servicio=None):


    cerda_dao = CerdaDAO()

    cerdas = cerda_dao.obtener_todos()



    # ==========================
    # CERDA
    # ==========================
    
    
    cerdas = [
     c for c in cerda_dao.obtener_todos()
     if c.estado == "Gestante" or c.estado == "Vacía" or c.estado == "Celo"
    ]

    cerda_input = ft.Dropdown(

        label="Número de arete de la cerda",

        width=300,

        options=[

            ft.dropdown.Option(

                key=str(cerda.id),

                text=cerda.arete

            )

            for cerda in cerdas

        ]

    )



    # ==========================
    # FECHA
    # ==========================


    fecha_input = ft.TextField(

        hint_text="AAAA-MM-DD",
            hint_style=ft.TextStyle(
                color="#9E9E9E",
                ),

        width=240,

        read_only=True

    )



    def seleccionar_fecha(e):

        if e.control.value:

            fecha_input.value = (
                e.control.value.strftime("%Y-%m-%d")
            )

            e.page.update()



    date_picker = ft.DatePicker(

        on_change=seleccionar_fecha

    )



    fecha_row = ft.Row(

        controls=[

            fecha_input,


            ft.IconButton(

                icon=ft.Icons.CALENDAR_MONTH,

                on_click=lambda e:
                e.page.show_dialog(date_picker)

            )

        ]

    )



    tipo_input = ft.Dropdown(
        hint_text="Monta natural",
                     hint_style=ft.TextStyle(
                color="#9E9E9E",
                ),
         width=300,
         options=[
            ft.dropdown.Option("Monta natural"),
            ft.dropdown.Option("Inseminación"),
         ]
        )
    # ==========================
    # CARGAR DATOS PARA EDITAR
    # ==========================

    if servicio:

        cerda_input.value = str(
            servicio.id_cerda
        )

        fecha_input.value = str(
            servicio.fecha_s
        )

        tipo_input.value = str(
            servicio.tipo
        )

        
    mensaje = ft.Text(
        "",
        color=ft.Colors.GREEN
    )



    # ==========================
    # GUARDAR / ACTUALIZAR
    # ==========================

    def guardar_servicio(e):


        if not cerda_input.value:


            mensaje.value = (
                "Seleccione una cerda"
            )

            mensaje.color = ft.Colors.RED

            e.page.update()

            return



        if not fecha_input.value:


            mensaje.value = (
                "Seleccione la fecha de servicio reproductivo"
            )

            mensaje.color = ft.Colors.RED

            e.page.update()

            return
        
        
                # ==========================
        # VALIDAR FECHA DE SERVICIO
        # ==========================

        cerda_id = int(cerda_input.value)

        destete_dao = DesteteDAO()

        fecha_destete = destete_dao.ultimo_destete(cerda_id)

        # Convertir la fecha del formulario
        fecha_servicio = datetime.strptime(
            fecha_input.value,
            "%Y-%m-%d"
        ).date()

        # Si la cerda ya tiene destetes registrados
        if fecha_destete:

            # En caso de que venga como datetime
            if isinstance(fecha_destete, datetime):
                fecha_destete = fecha_destete.date()

            # Fecha mínima permitida (3 días después del destete)
            fecha_minima = fecha_destete + timedelta(days=3)

            if fecha_servicio < fecha_minima:

                dias = (fecha_servicio - fecha_destete).days

                mensaje.value = (
                    f"El servicio solo puede registrarse 3 días después del último destete. "
                    f"Solo han transcurrido {dias} días."
                )

                mensaje.color = ft.Colors.RED
                e.page.update()
                return
            
        
        if not tipo_input.value:
        
        
                    mensaje.value = (
                        "Seleccione un tipo de servicio reproductivo"
                    )
        
                    mensaje.color = ft.Colors.RED
        
                    e.page.update()
        
                    return



        


    



        cerda_id = int(
            cerda_input.value
        )



        servicio_dao = ServicioDAO()



        # ==========================
        # EDITAR
        # ==========================

        if servicio:


            servicio.id_cerda = cerda_id

            servicio.fecha_s = fecha_input.value

            servicio.tipo = tipo_input.value

          

            servicio_dao.actualizar(
                servicio
            )


            regresar(
               f"Servicio reproductivo {servicio.id_servicio} actualizado correctamente"
            ) 
            
            



        # ==========================
        # NUEVO
        # ==========================

        else:


            nuevo_servicio = Servicio(

                None,

                cerda_id,
            

                fecha_input.value,

                tipo_input.value

            )


            servicio_dao.insertar(
                nuevo_servicio
            )



            # Cambiar estado cerda

            cerda = (
                cerda_dao.obtener_por_id(
                    cerda_id
                )
            )


            if cerda:

                cerda.estado = "Gestante"

                cerda_dao.actualizar(
                    cerda
                )



            regresar(
             "Servicio reproductivo registrado correctamente"
             )



      
        
        




    # ==========================
    # BOTONES
    # ==========================


    botones = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15,
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

          "Guardar" if servicio else "Registrar",

           icon=(
         ft.Icons.SAVE
         if servicio
         else ft.Icons.ADD
         ),

          style=ft.ButtonStyle(
         bgcolor="#E85A8E",
         color=ft.Colors.WHITE
          ),


                on_click=guardar_servicio

            )

        ]

    )



    # ==========================
    # VISTA
    # ==========================


    return ft.Container(
        width=720,
        padding=30,
        bgcolor="white",
        border_radius=8,


        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,


            controls=[


                ft.Text(
                    
                    "Editar información de reproducción" if servicio else "Registro de Reproducción",

                    size=25,

                    weight=ft.FontWeight.BOLD

                ),



                ft.Text(

                    "Capture los datos básicos del servicio reproductivo",

                    size=14

                ),

                ft.Divider(),
                
                ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Número de arete de la cerda:", width=200),
                        cerda_input
                    ]
                ),

                ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Fecha de servicio:", width=200),
                        fecha_row
                    ]
                ),
                
                ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Fecha de servicio:", width=200),
                        tipo_input,
                    ]
                ),

                ft.Divider(),



                mensaje,


                botones


            ]

        )

    )