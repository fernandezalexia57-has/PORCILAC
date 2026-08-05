import datetime

import flet as ft


from dao.servicio_dao import ServicioDAO
from models.parto import Parto
from dao.parto_dao import PartoDAO
from dao.cerda_dao import CerdaDAO



def parto_form(regresar, parto=None):


    cerda_dao = CerdaDAO()

    cerdas = cerda_dao.obtener_todos()



    # ==========================
    # CERDA
    # ==========================
    
    cerdas = [
         c for c in cerda_dao.obtener_todos()
         if c.estado == "Gestante"
         ]

    cerda_input = ft.Dropdown(

        label="Número de arete de la cerda",

        width=400,

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

        label="Fecha del parto",

        hint_text="AAAA/MM/DD",

        width=340,

        read_only=True

    )



    def seleccionar_fecha(e):

        if e.control.value:

            fecha_input.value = (
                e.control.value.strftime("%Y/%m/%d")
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



    # ==========================
    # LECHONES
    # ==========================


    vivos_input = ft.TextField(

        label="Lechones vivos",

        value="0",

        width=300,

        read_only=True,

        text_align=ft.TextAlign.CENTER

    )



    muertos_input = ft.TextField(

        label="Lechones muertos",
         

        value="0",

        width=300,

        read_only=True,

        text_align=ft.TextAlign.CENTER

    )



    num_le_input = ft.TextField(

        label="Número de lechones",

        value="0",

        width=300,

        read_only=True,

        text_align=ft.TextAlign.CENTER

    )
    
    observaciones_input = ft.TextField(
     label="Observaciones",
     hint_text="Escriba aquí las observaciones del parto...",
     width=400,
     multiline=True,
     min_lines=1,
     max_lines=2
    )



    def actualizar_total():

        total = (

            int(vivos_input.value)

            +

            int(muertos_input.value)

        )


        num_le_input.value = str(total)



    # ==========================
    # CONTADORES
    # ==========================


    def aumentar_vivos(e):

        vivos_input.value = str(

            int(vivos_input.value) + 1

        )

        actualizar_total()

        e.page.update()



    def disminuir_vivos(e):

        if int(vivos_input.value) > 0:

            vivos_input.value = str(

                int(vivos_input.value)-1

            )

            actualizar_total()

            e.page.update()



    vivos_row = ft.Row(

        controls=[

            vivos_input,


            ft.IconButton(

                icon=ft.Icons.REMOVE,

                on_click=disminuir_vivos

            ),


            ft.IconButton(

                icon=ft.Icons.ADD,

                icon_color=ft.Colors.GREEN,

                on_click=aumentar_vivos

            )

        ]

    )



    def aumentar_muertos(e):

        muertos_input.value = str(

            int(muertos_input.value)+1

        )

        actualizar_total()

        e.page.update()



    def disminuir_muertos(e):

        if int(muertos_input.value)>0:

            muertos_input.value = str(

                int(muertos_input.value)-1

            )

            actualizar_total()

            e.page.update()



    muertos_row = ft.Row(

        controls=[

            muertos_input,


            ft.IconButton(

                icon=ft.Icons.REMOVE,

                on_click=disminuir_muertos

            ),


            ft.IconButton(

                icon=ft.Icons.ADD,

                icon_color=ft.Colors.GREEN,

                on_click=aumentar_muertos

            )

        ]

    )
    # ==========================
    # CARGAR DATOS PARA EDITAR
    # ==========================

    if parto:

        cerda_input.value = str(
            parto.id_cerda
        )

        fecha_input.value = str(
            parto.fecha
        )

        num_le_input.value = str(
            parto.num_le
        )

        vivos_input.value = str(
            parto.lechones_v
        )

        muertos_input.value = str(
            parto.lechones_m
        )
        observaciones_input.value = str(
            parto.observaciones
        )



    mensaje = ft.Text(
        "",
        color=ft.Colors.GREEN
    )



    # ==========================
    # GUARDAR / ACTUALIZAR
    # ==========================

    def guardar_parto(e):


        if not cerda_input.value:


            mensaje.value = (
                "Seleccione una cerda"
            )

            mensaje.color = ft.Colors.RED

            e.page.update()

            return
        

        if not fecha_input.value:


            mensaje.value = (
                "Seleccione la fecha del parto"
            )

            mensaje.color = ft.Colors.RED

            e.page.update()

            return
    
        cerda_id = int(cerda_input.value)

        cerda = cerda_dao.obtener_por_id(cerda_id)


        servicio_dao = ServicioDAO()

        fecha_servicio = servicio_dao.ultimo_servicio(cerda_id)

        if fecha_servicio:

         fecha_parto = datetime.strptime(
         fecha_input.value,
         "%Y/%m/%d"
            ).date()

         dias = (fecha_parto - fecha_servicio).days

         if dias < 111:

            mensaje.value = (
             f"El parto no puede registrarse antes de los 111 días del servicio. "
             f"Solo han transcurrido {dias} días."
            
            )
            mensaje.color = ft.Colors.RED

            e.page.update()

            return
          
         if dias > 120:
              
            mensaje.value = (
            f"Han transcurrido {dias} días desde el servicio. "
            "Verifique que la fecha del parto sea correcta."
            )
        


            mensaje.color = ft.Colors.RED

            e.page.update()

            return



        total_lechones = int(
            num_le_input.value
        )


        if total_lechones <= 0:


            mensaje.value = (
                "Debe registrar al menos un lechón"
            )

            mensaje.color = ft.Colors.RED

            e.page.update()

            return



        cerda_id = int(
            cerda_input.value
        )



        parto_dao = PartoDAO()



        # ==========================
        # EDITAR
        # ==========================

        if parto:


            parto.id_cerda = cerda_id

            parto.fecha = fecha_input.value

            parto.num_le = total_lechones

            parto.lechones_v = int(
                vivos_input.value
            )

            parto.lechones_m = int(
                muertos_input.value
            )
            
            parto.observaciones = observaciones_input.value


            parto_dao.actualizar(
                parto
            )


            regresar(
             f"Parto {parto.id_parto} actualizado correctamente"
             )
            
            



        # ==========================
        # NUEVO
        # ==========================

        else:


            nuevo_parto = Parto(

                None,

                cerda_id,

                fecha_input.value,

                total_lechones,

                int(vivos_input.value),

                int(muertos_input.value),
                
                observaciones_input.value

            )


            parto_dao.insertar(
                nuevo_parto
            )



            # Cambiar estado cerda

            cerda = (
                cerda_dao.obtener_por_id(
                    cerda_id
                )
            )


            if cerda:

                cerda.estado = "Lactante"

                cerda_dao.actualizar(
                    cerda
                )



            regresar(
                "Parto registrado correctamente"
            )



       
        
        




    # ==========================
    # BOTONES
    # ==========================


    botones = ft.Row(

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

          "Actualizar parto" if parto else "Registrar parto",

           icon=(
         ft.Icons.SAVE
         if parto
         else ft.Icons.ADD
         ),

          style=ft.ButtonStyle(
         bgcolor="#E85A8E",
         color=ft.Colors.WHITE
          ),


                on_click=guardar_parto

            )

        ]

    )



    # ==========================
    # VISTA
    # ==========================


    return ft.Container(

        padding=30,


        content=ft.Column(

            spacing=10,


            controls=[


                ft.Text(

                    "Registro de parto",

                    size=25,

                    weight=ft.FontWeight.BOLD

                ),



                ft.Text(

                    "Capture los datos básicos del parto",

                    size=14

                ),

                ft.Divider(),

                cerda_input,


                fecha_row,
        

                vivos_row,


                muertos_row,


                num_le_input,
                
                observaciones_input,



                ft.Divider(),



                mensaje,


                botones


            ]

        )

    )