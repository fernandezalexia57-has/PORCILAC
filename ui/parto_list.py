import flet as ft

from dao.parto_dao import PartoDAO



def parto_list(nuevo_parto, editar_parto):


    parto_dao = PartoDAO()


    # ==========================
    # DATOS
    # ==========================

    todos_partos = parto_dao.obtener_todos()

    partos_filtrados = todos_partos.copy()


    pagina_actual = {
        "valor": 1
    }


    por_pagina = 3



    # ==========================
    # TARJETA PARTO
    # ==========================

    def crear_tarjeta(parto, editar_parto):

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
                        f"ID de parto: {parto.id_parto}",
                        size=14
                    ),


                    ft.Text(
                        f"Num. Arete de la cerda: {parto.arete}",
                        size=14
                    ),


                    ft.Text(
                        f"Fecha de parto: {parto.fecha}",
                        size=14
                    ),


                    ft.Text(
                        f"Num. de lechones: {parto.num_le}",
                        size=14
                    ),


                    ft.Text(
                        f"Lechones vivos: {parto.lechones_v}",
                        size=14
                    ),


                    ft.Text(
                        f"Lechones muertos: {parto.lechones_m}",
                        size=14
                    ),


                    ft.Text(
                        f"Observaciones: {parto.observaciones}",
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

                                on_click=lambda e:
                                editar_parto(parto)

                            )


                        ]

                    )


                ]

            )

        )



    # ==========================
    # TARJETAS
    # ==========================


    lista_tarjetas = ft.GridView(

     
     expand=True,

     runs_count=3,

     max_extent=350,

     spacing=35,

     run_spacing=35,

     child_aspect_ratio=0.90

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
                len(partos_filtrados)
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



        for parto in partos_filtrados[inicio:fin]:


            lista_tarjetas.controls.append(

                crear_tarjeta(
                    parto,
                    editar_parto
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

        hint_text="Buscar parto por (Núm. Arete, Fecha)",
        hint_style=ft.TextStyle(
                    color="#9E9E9E",
                    ),

        width=370,

        height=48,

        prefix_icon=ft.Icons.SEARCH

    )



    dropdown_filtro = ft.Dropdown(
        width=235,
        value="Todos",
        options=[
            ft.dropdown.Option("Todos"),
            ft.dropdown.Option("Con lechones muertos"),
            ft.dropdown.Option("Sin lechones muertos"),
            ft.dropdown.Option("Más de 10 lechones"),
            ft.dropdown.Option("10 lechones o menos")
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

        texto = buscador.value.lower().strip()

        partos_filtrados.clear()

        for p in todos_partos:

            if (
                texto in str(p.arete).lower()
                or texto in str(p.fecha).lower()
            ):

                partos_filtrados.append(p)

        pagina_actual["valor"] = 1

        cargar_tarjetas()

        cargar_paginacion()

        e.page.update()


    def aplicar_filtro(e):
        print(dropdown_filtro.value)

        opcion = dropdown_filtro.value

        partos_filtrados.clear()

        if opcion == "Todos":

            partos_filtrados.extend(todos_partos)

        elif opcion == "Con lechones muertos":

            for p in todos_partos:

                if p.lechones_m > 0:

                    partos_filtrados.append(p)

        elif opcion == "Sin lechones muertos":

            for p in todos_partos:

                if p.lechones_m == 0:

                    partos_filtrados.append(p)

        elif opcion == "Más de 10 lechones":

            for p in todos_partos:

                if p.num_le > 10:

                    partos_filtrados.append(p)

        elif opcion == "10 lechones o menos":

            for p in todos_partos:

                if p.num_le <= 10:

                    partos_filtrados.append(p)

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

                alignment=ft.MainAxisAlignment.CENTER,

                controls=[

                    ft.Text(
                        "Partos",
                        size=32,
                        weight=ft.FontWeight.BOLD
                    )

                ]

            ),



            ft.Row(

                alignment=ft.MainAxisAlignment.CENTER,

                spacing=30,

                controls=[

                    buscador,

                    filtro,


                    ft.ElevatedButton(

                        "+ Nuevo parto",

                        height=48,

                        bgcolor="#E85A8E",

                        color="white",

                        on_click=lambda e:
                        nuevo_parto()

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