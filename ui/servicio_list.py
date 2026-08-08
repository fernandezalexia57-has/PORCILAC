import flet as ft

from dao.servicio_dao import ServicioDAO



def servicio_list(nuevo_servicio, editar_servicio):


    servicio_dao = ServicioDAO()



    # ==========================
    # DATOS
    # ==========================

    todos_servicios = servicio_dao.obtener_todos()

    servicios_filtrados = todos_servicios.copy()


    pagina_actual = {
        "valor": 1
    }


    por_pagina = 3



    # ==========================
    # TARJETA PARTO
    # ==========================

    def crear_tarjeta(servicio, editar_servicio):

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
                        f"ID de servicio: {servicio.id_servicio}",
                        size=14
                    ),


                    ft.Text(
                        f"Num. Arete de la cerda: {servicio.arete}",
                        size=14
                    ),


                    ft.Text(
                        f"Fecha de servicio: {servicio.fecha_s}",
                        size=14
                    ),


                    ft.Text(
                        f"Tipo de servicio: {servicio.tipo}",
                        size=14
                    ),


                  
                    ft.Row(

                        alignment=
                        ft.MainAxisAlignment.CENTER,
                        

                        controls=[


                            ft.ElevatedButton(

                                "Editar",

                                icon=ft.Icons.EDIT,


                                style=ft.ButtonStyle(

                                    bgcolor="#55B87A",

                                    color="white",


                                    shape=
                                    ft.RoundedRectangleBorder(
                                        radius=20
                                    )

                                ),
                                 on_click=lambda e: editar_servicio(servicio)

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

    runs_count=3,          # cantidad de tarjetas por fila

    max_extent=350,        # ancho máximo de cada tarjeta

    spacing=35,            # separación horizontal

    run_spacing=35,        # separación vertical

    child_aspect_ratio=0.90

)
    contenedor_tarjetas = ft.Container(

    alignment=ft.Alignment(0, 0),

    content=lista_tarjetas,

     )


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
                len(servicios_filtrados)
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



        for servicio in servicios_filtrados[inicio:fin]:


            lista_tarjetas.controls.append(

                crear_tarjeta(
                    servicio,
                    editar_servicio
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
        "Buscar servicio por (Núm. Arete, Fecha)",
        hint_style=ft.TextStyle(
                    color="#9E9E9E",
                    ),
        width=370,
        height= 48,

        prefix_icon=ft.Icons.SEARCH

    )



    dropdown_filtro = ft.Dropdown(

        width=235,

        value="Todos",

        options=[

            ft.dropdown.Option("Todos"),

            ft.dropdown.Option("Inseminación"),

            ft.dropdown.Option("Monta natural")

        ]

    )
    
    filtro = ft.Row(
        spacing=8,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Icon(
                ft.Icons.FILTER_ALT,
                color="#5B6375",
                size=48
            ),
            dropdown_filtro
        ]
    )
   


    def buscar(e):


        texto = (
            buscador.value
            .lower()
        )


        servicios_filtrados.clear()



        for p in todos_servicios:


            if (

                texto in str(
                    p.arete
                ).lower()


                or texto in str(
                    p.fecha_s
                ).lower()


            ):


                servicios_filtrados.append(p)




        pagina_actual["valor"] = 1


        cargar_tarjetas()
        cargar_paginacion()


    def aplicar_filtro(e):

        opcion = e.control.value


        servicios_filtrados.clear()



        for s in todos_servicios:


            if opcion == "Todos":

                servicios_filtrados.append(s)



            elif opcion == "Inseminación":


                if s.tipo.lower() == "inseminación":

                    servicios_filtrados.append(s)




            elif opcion == "Monta natural":


                if s.tipo.lower() == "monta natural":

                    servicios_filtrados.append(s)




        pagina_actual["valor"] = 1


        cargar_tarjetas()

        cargar_paginacion()

        e.page.update()
        
        

    buscador.on_change = buscar
    dropdown_filtro.on_select = aplicar_filtro
    
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

                            "Reproducción",

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

                            "+ Nuevo preño",
                               height=48,


                            bgcolor="#E85A8E",

                            color="white",


                            on_click=
                            lambda e:
                            nuevo_servicio()

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