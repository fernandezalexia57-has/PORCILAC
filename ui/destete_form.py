from tokenize import Double

import flet as ft

from models.destete import Destete
from dao.destete_dao import DesteteDAO
from dao.cerda_dao import CerdaDAO
from dao.parto_dao import PartoDAO
from datetime import datetime



def destete_form(regresar, destete=None):


    cerda_dao = CerdaDAO()

    cerdas = cerda_dao.obtener_todos()



    # ==========================
    # CERDA
    # ==========================
    
    
    cerdas = [
     c for c in cerda_dao.obtener_todos()
     if c.estado == "Lactante"
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

        label="Fecha del destete",

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


    numle_input = ft.TextField(

        label=" Número de lechones",

        value="0",

        width=300,

        read_only=True,

        text_align=ft.TextAlign.CENTER

    )
    
    
    peso_input = ft.TextField(
            label ="Peso promedio (kg): ",
            hint_text="12.100",
            width= 400
        )
    
    
    
    







    # ==========================
    # CONTADORES
    # ==========================



    def aumentar_numle(e):

        numle_input.value = str(

            int(numle_input.value)+1

        )




    def disminuir_numle(e):

        if int(numle_input.value)>0:

            numle_input.value = str(

                int(numle_input.value)-1

            )


            e.page.update()



    numle_row = ft.Row(

        controls=[

            numle_input,


            ft.IconButton(

                icon=ft.Icons.REMOVE,

                on_click=disminuir_numle

            ),


            ft.IconButton(

                icon=ft.Icons.ADD,

                icon_color=ft.Colors.GREEN,

                on_click=aumentar_numle

            )

        ]

    )
    # ==========================
    # CARGAR DATOS PARA EDITAR
    # ==========================

    if destete:

        cerda_input.value = str(
            destete.id_cerda
        )

        fecha_input.value = str(
            destete.fecha_d
        )

        numle_input.value = str(
            destete.numle
        )
        
        peso_input.value = str(
                    destete.peso
                )



    mensaje = ft.Text(
        "",
        color=ft.Colors.GREEN
    )



    # ==========================
    # GUARDAR / ACTUALIZAR
    # ==========================

    def guardar_destete(e):


        if not cerda_input.value:


            mensaje.value = (
                "Seleccione una cerda"
            )

            mensaje.color = ft.Colors.RED

            e.page.update()

            return
        
        

        if not fecha_input.value:


            mensaje.value = (
                "Seleccione la fecha del destete"
            )

            mensaje.color = ft.Colors.RED

            e.page.update()

            return

        cerda_id = int(cerda_input.value)

        parto_dao = PartoDAO()

        fecha_parto = parto_dao.ultimo_parto(cerda_id)

        if fecha_parto:

            fecha_destete = datetime.strptime(
             fecha_input.value,
            "%Y/%m/%d"
            ).date()

            dias = (fecha_destete - fecha_parto).days

            if dias < 21:

                mensaje.value = (
                f"El destete no puede registrarse antes de los 21 días del parto. "
                f"Solo han transcurrido {dias} días."
                )

                mensaje.color = ft.Colors.RED
                e.page.update()
                return

            if dias > 35:

                mensaje.value = (
                 f"Han transcurrido {dias} días desde el parto. "
                "Verifique que la fecha del destete sea correcta."
                )

                mensaje.color = ft.Colors.RED
                e.page.update()
                return




        numle= int(
            numle_input.value
        )


        if numle <= 0:


            mensaje.value = (
                "Debe registrar al menos un lechón"
            )

            mensaje.color = ft.Colors.RED

            e.page.update()

            return

        cerda_id = int(cerda_input.value)

        parto_dao = PartoDAO()
        
        lechones_vivos = parto_dao.ultimo_lechones_vivos(cerda_id)

        if int(numle_input.value) > lechones_vivos:

            mensaje.value = (
                f"No puede registrar {numle_input.value} lechones destetados. "
                f"El último parto tuvo únicamente {lechones_vivos} lechones vivos."
            )

            mensaje.color = ft.Colors.RED
            e.page.update()
            return
        
        if not peso_input.value:
                
                
            mensaje.value = (
            "Escriba un peso promedio en kilogramos"
            )
                
            mensaje.color = ft.Colors.RED
                
            e.page.update()
                
            return



        cerda_id = int(
            cerda_input.value
        )



        destete_dao = DesteteDAO()



        # ==========================
        # EDITAR
        # ==========================

        if destete:


            destete.id_cerda = cerda_id

            destete.fecha = fecha_input.value

            

            destete.numle = int(
                numle_input.value
            )

            
            
            destete.peso = float(peso_input.value)


            destete_dao.actualizar(
                destete
            )


            regresar(
             f"Destete {destete.id_destete} actualizado correctamente"
            )
            
            



        # ==========================
        # NUEVO
        # ==========================

        else:


            nuevo_destete = Destete(

                None,

                cerda_id,

                fecha_input.value,

                int(numle_input.value),
                
                float(peso_input.value)

            )


            destete_dao.insertar(
                nuevo_destete
            )



            # Cambiar estado cerda

            cerda = (
                cerda_dao.obtener_por_id(
                    cerda_id
                )
            )


            if cerda:

                cerda.estado = "Vacía"

                cerda_dao.actualizar(
                    cerda
                )



            regresar(
                "Destete registrado correctamente"
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

          "Actualizar destete" if destete else "Registrar destete",

           icon=(
         ft.Icons.SAVE
         if destete
         else ft.Icons.ADD
         ),

          style=ft.ButtonStyle(
         bgcolor="#E85A8E",
         color=ft.Colors.WHITE
          ),


                on_click=guardar_destete

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

                    "Registro de destete",

                    size=25,

                    weight=ft.FontWeight.BOLD

                ),



                ft.Text(

                    "Capture los datos básicos del destete",

                    size=14

                ),

                ft.Divider(),

                cerda_input,


                fecha_row,
        

                numle_row,
                
                peso_input,
                
                



                ft.Divider(),



                mensaje,


                botones


            ]

        )

    )