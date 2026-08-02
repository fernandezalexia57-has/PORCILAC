


from tkinter import dialog

import flet as ft

from dao.cerda_dao import CerdaDAO



def cerda_list(nuevo_cerda, editar_cerda, ver_detalles):


    cerda_dao = CerdaDAO()
   
    
    
    
    # ==========================
    # DATOS
    # ==========================

    todos_cerdas = cerda_dao.obtener_todos()

    cerdas_filtrados = todos_cerdas.copy()


    pagina_actual = {
        "valor": 1
    }


    por_pagina = 2



    # ==========================
    # TARJETA PARTO
    # ==========================

    def crear_tarjeta(cerda, editar_cerda):
        # ==========================
        # COLOR SEGÚN ESTADO
        # ==========================

        colores_estado = {
        "Celo": "#C08552",
        "Gestante": "#5CB87A",
        "Lactante": "#E8618C",
        "Vacía": "#5C8DB8",
         "Baja": "#9E9E9E"
        }

        color_estado = colores_estado.get(cerda.estado, "#D9D9D9")
        
        

        return ft.Container(

            width=300,

            height=220,

             padding=10,

             bgcolor="white",

             border_radius=12,
             
             shadow=ft.BoxShadow(
             
                    blur_radius=10,
             
                    color="#D9D9D9",
             
                    offset=ft.Offset(0,3)
             
                     ),

            

            content=ft.Column(

                spacing=1,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,


                controls=[


                    ft.Text(
                        f"ID cerda: {cerda.id}",
                        size=14
                    ),


                    ft.Text(
                        f"Num. Arete: {cerda.arete}",
                        size=14
                    ),
                    
                    
                    ft.Text(
                        f"Raza: {cerda.raza}",
                        size=14
                    ),
                    
                    
                    ft.Text(
                        f"Color: {cerda.color}",
                        size=14
                    ),
                    
                    
                         ft.Text(
                        f"Edad: {cerda.edad} años",
                        size=14
                    ),
                    
                    ft.Row(
                        
                        controls=[

                        ft.Text(
                      "Estado reproductivo:",
                         size=14
                         ),

                        ft.Container(
                            padding=10,
                             bgcolor=color_estado,
                            border_radius=20,
                            content=ft.Text(
                            cerda.estado,
                            color=ft.Colors.WHITE,
                             weight=ft.FontWeight.BOLD,
                             size=12,
                            ),
                            )

                            ]
                        ),


                    ft.Text(
                        f"Fecha de registro: {cerda.fecha}",
                        size=14
                    ),




                  
                    ft.Row(
                        
                        alignment=
                        ft.MainAxisAlignment.CENTER,
                        

                        controls=[
                            
                            
                            ft.ElevatedButton(
                                "Ver historial",
                                icon=ft.Icons.VISIBILITY,
                                bgcolor="#5C8DB8",
                                color="white",
                                on_click=lambda e: ver_detalles(cerda)
                            ),
                             



                            ft.ElevatedButton(

                                "Editar",

                                icon=ft.Icons.EDIT,
                                disabled=(cerda.estado == "Baja"),


                                style=ft.ButtonStyle(

                                    bgcolor="#55B87A",

                                    color="white",


                                    shape=
                                    ft.RoundedRectangleBorder(
                                        radius=20
                                    )

                                ),
                                 on_click=lambda e: editar_cerda(cerda)
                                 
                            ),
                            
                             
                                 
                            ft.ElevatedButton(
                                "Dar de baja",
                                
                                disabled=(cerda.estado == "Baja"),
                                
                                style=ft.ButtonStyle(

                                    bgcolor="#E8618C",

                                    color="white",


                                    shape=
                                    ft.RoundedRectangleBorder(
                                        radius=20
                                    )

                                   ),
                                     on_click=lambda e, cerda_id=cerda.id:
                                    confirmar_baja(e, cerda_id)
                                )

                        ]

                    )

                ]

            )

        )



    # ==========================
    # CONTENEDOR TARJETAS
    # ==========================


    lista_tarjetas = ft.GridView(

    expand=True,

    runs_count=2,          # cantidad de tarjetas por fila

    max_extent=500,        # ancho máximo de cada tarjeta

    spacing=35,            # separación horizontal

    run_spacing=35,        # separación vertical

    child_aspect_ratio=1.41

)
    contenedor_tarjetas = ft.Container(

    alignment=ft.Alignment(0, 0),

    content=lista_tarjetas,

     )
    
    # ==========================
    # DAR DE BAJA CERDA
    # ==========================
    def confirmar_baja(e, id):

        def aceptar(ev):

            cerda_dao.dar_baja(id)

            dialog.open = False
            
            mensaje = ft.SnackBar(
             content=ft.Text(
            "Cerda dada de baja correctamente"
             )
            )

            e.page.overlay.append(mensaje)

            mensaje.open = True
            e.page.update()

            todos_cerdas.clear()
            todos_cerdas.extend(
            cerda_dao.obtener_todos()
            )

            cerdas_filtrados.clear()
            cerdas_filtrados.extend(
            todos_cerdas
            )

            cargar_tarjetas()
            cargar_paginacion()

            lista_tarjetas.update()


        def cancelar(ev):

            dialog.open = False
            e.page.update()


        dialog = ft.AlertDialog(

            title=ft.Text(
            "Dar de baja cerda"
            ),

         content=ft.Text(
            "¿Está seguro que desea dar de baja esta cerda?"
         ),

         actions=[

            ft.TextButton(
                "Cancelar",
                on_click=cancelar
            ),

            ft.TextButton(
                "Aceptar",
                on_click=aceptar
            )

        ]
    )


        e.page.overlay.append(dialog)

        dialog.open = True

        e.page.update()

    # ==========================
    # PAGINACION
    # ==========================


    paginacion = ft.Row(

        alignment=ft.MainAxisAlignment.CENTER,

        spacing=5

    )



    def total_paginas():

        return max(
            1,
            (
                len(cerdas_filtrados)
                +
                por_pagina
                -
                1
            )
            //
            por_pagina
        )



    def cargar_tarjetas():


        inicio = (

            pagina_actual["valor"]
            -
            1

        ) * por_pagina



        fin = inicio + por_pagina



        lista_tarjetas.controls.clear()



        for cerda in cerdas_filtrados[inicio:fin]:


            lista_tarjetas.controls.append(

                crear_tarjeta(
                    cerda,
                    editar_cerda
                )

            )




    def cargar_paginacion():
        print("Total páginas:", total_paginas())


        paginacion.controls.clear()



        # ==========================
        # ANTERIOR
        # ==========================


        paginacion.controls.append(

            ft.OutlinedButton(

                "Anterior",

                on_click=anterior,

                style=ft.ButtonStyle(

                    color=ft.Colors.BLACK,

                    side=ft.BorderSide(
                        1,
                        ft.Colors.BLACK
                    )

                )

            )

        )



        # ==========================
        # NUMEROS
        # ==========================


        for i in range(
            1,
            total_paginas()+1
        ):


            boton = ft.Container(


                width=35,

                height=35,


                border_radius=5,


                alignment=ft.Alignment(0,0),



                bgcolor=(

                    "#E85A8E"

                    if i ==
                    pagina_actual["valor"]

                    else
                    "white"

                ),



                border=ft.Border(

                    left=ft.BorderSide(
                        1,
                        "#E85A8E"
                    ),

                    right=ft.BorderSide(
                        1,
                        "#E85A8E"
                    ),

                    top=ft.BorderSide(
                        1,
                        "#E85A8E"
                    ),

                    bottom=ft.BorderSide(
                        1,
                        "#E85A8E"
                    )

                ),



                content=ft.Text(

                    str(i),

                    color=(

                        "white"

                        if i ==
                        pagina_actual["valor"]

                        else
                        "black"

                    ),

                    weight=ft.FontWeight.BOLD

                ),



                on_click=lambda e, pagina=i:

                    cambiar_pagina(pagina)

            )



            paginacion.controls.append(

                boton

            )





        # ==========================
        # SIGUIENTE
        # ==========================


        paginacion.controls.append(

            ft.OutlinedButton(

                "Siguiente",

                on_click=siguiente,

                style=ft.ButtonStyle(

                    color=ft.Colors.BLACK,

                    side=ft.BorderSide(
                        1,
                        ft.Colors.BLACK
                    )

                )

            )

        )






    def cambiar_pagina(pagina):


        pagina_actual["valor"] = pagina


        cargar_tarjetas()

        cargar_paginacion()




    def anterior(e):


        if pagina_actual["valor"] > 1:


            pagina_actual["valor"] -= 1


            cargar_tarjetas()

            cargar_paginacion()


            e.page.update()






    def siguiente(e):


        if pagina_actual["valor"] < total_paginas():


            pagina_actual["valor"] += 1


            cargar_tarjetas()

            cargar_paginacion()


            e.page.update()






    # ==========================
    # BUSCADOR
    # ==========================


    buscador = ft.TextField(

        hint_text=
        "Buscar cerda(ID, Núm. Arete)",

        width=370,
        height= 48,

        prefix_icon=ft.Icons.SEARCH

    )



    filtro = ft.Dropdown(

        width=150,

        value="Todos",

        options=[


            ft.dropdown.Option(
                "Todos"
            ),


            ft.dropdown.Option(
                "Fecha de registro"
            ),


            


        ]

    )
   


    def buscar(e):


        texto = (
            buscador.value
            .lower()
        )


        cerdas_filtrados.clear()



        for p in todos_cerdas:


            if (

                texto in str(
                    p.id
                )


                or texto in str(
                    p.arete
                ).lower()


                or texto in str(
                    p.fecha
                ).lower()


               


            ):


                cerdas_filtrados.append(p)




        pagina_actual["valor"] = 1


        cargar_tarjetas()
        cargar_paginacion()




    buscador.on_change = buscar
    
    cargar_tarjetas()
    cargar_paginacion()




    # ==========================
    # VISTA FINAL
    # ==========================


    return ft.Container(

        expand=True,

        bgcolor="#FFFFFF",

        padding=30,


        content=ft.Column(

            spacing=20,
            expand=True,
            


            controls=[



                ft.Row(

                    alignment=
                    ft.MainAxisAlignment.CENTER,


                    controls=[


                        ft.Text(

                            "Cerdas",

                            size=32,

                            weight=
                            ft.FontWeight.BOLD

                        )

                    ]

                ),




                ft.Row(

                      alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=30,


                    controls=[


                        buscador,


                        filtro,



                        ft.ElevatedButton(

                            "+ Nueva cerda",
                               height=48,


                            bgcolor="#E85A8E",

                            color="white",


                            on_click=
                            lambda e:
                            nuevo_cerda()

                        )


                    ]

                ),




                ft.Divider(),




                 ft.Container(
                
                
                    content=lista_tarjetas
                
                 ),



                 ft.Container(
                
                    height=60,
                
                    content=paginacion,
                
                    alignment=ft.Alignment(0,0)
                
                 )



            ]

        )

    )