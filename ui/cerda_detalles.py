import flet as ft

from datetime import datetime, timedelta

from dao.servicio_dao import ServicioDAO
from dao.parto_dao import PartoDAO
from dao.destete_dao import DesteteDAO



def cerda_detalles(cerda, regresar):


    servicio_dao = ServicioDAO()
    parto_dao = PartoDAO()
    destete_dao = DesteteDAO()


    # ==========================
    # RESUMEN REPRODUCTIVO
    # ==========================

    total_servicios = servicio_dao.total_servicios(
        cerda.id
    )

    total_partos = parto_dao.total_partos(
        cerda.id
    )

    total_destetes = destete_dao.total_destetes(
        cerda.id
    )

    lechones_vivos = parto_dao.total_lechones_vivos(
        cerda.id
    )

    lechones_muertos = parto_dao.total_lechones_muertos(
        cerda.id
    )

    lechones_destetados = destete_dao.total_lechones_destetados(
        cerda.id
    )


    ultimo_servicio = servicio_dao.ultimo_servicio(
        cerda.id
    )

    ultimo_parto = parto_dao.ultimo_parto(
        cerda.id
    )

    ultimo_destete = destete_dao.ultimo_destete(
        cerda.id
    )



    # ==========================
    # CALCULAR PROXIMOS EVENTOS
    # ==========================


    posible_parto = None
    posible_destete = None
    proximo_servicio = None



    if ultimo_servicio:


        fecha_servicio = datetime.strptime(
            str(ultimo_servicio),
            "%Y-%m-%d"
        )


        posible_parto = (
            fecha_servicio
            +
            timedelta(days=114)
        )



    if ultimo_parto:


        fecha_parto = datetime.strptime(
            str(ultimo_parto),
            "%Y-%m-%d"
        )


        posible_destete = (
            fecha_parto
            +
            timedelta(days=28)
        )



    if ultimo_destete:


        fecha_destete = datetime.strptime(
            str(ultimo_destete),
            "%Y-%m-%d"
        )


        proximo_servicio = (
            fecha_destete
            +
            timedelta(days=7)
        )



    # ==========================
    # TARJETA INDICADOR
    # ==========================


    def indicador(titulo, valor):
        
        colores_indicadores = {

        "Servicios": "#5C8DB8",
        "Partos": "#5CB87A",
        "Destetes": "#E8618C",
        "Vivos": "#55B87A",
        "Muertos": "#C08552",
        "Destetados": "#6B4A32"

        }

        return ft.Container(

            width=120,

            padding=10,

            bgcolor=colores_indicadores.get(
            titulo,
            "#D9D9D9"
            ),

            border_radius=12,

            content=ft.Column(

                horizontal_alignment=
                ft.CrossAxisAlignment.CENTER,

                controls=[

                    ft.Text(
                        titulo,
                        size=12,
                        color="white"
                    ),

                    ft.Text(
                        str(valor),
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color="white"
                    )

                ]

            )

        )



    # ==========================
    # VISTA
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

        padding=30,

        expand=True,

        content=ft.Column(

            scroll=ft.ScrollMode.AUTO,

            spacing=20,

            controls=[



                ft.Text(
                    "Ficha de la cerda",
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),



                # DATOS GENERALES

                ft.Container(

                    width=300,
                    
                    height=250,
                    
                    padding=10,
                    
                    bgcolor="white",
                    
                    border_radius=12,
                                 
                    shadow=ft.BoxShadow(
                                 
                    blur_radius=10,
                                 
                    color="#D9D9D9",
                                 
                    offset=ft.Offset(0,3)
                                 
                    ),

                    content=ft.Column(

                        controls=[


                            ft.Text(
                                "Datos generales",
                                size=20,
                                weight=ft.FontWeight.BOLD
                            ),


                            ft.Text(
                                f"Arete: {cerda.arete}"
                            ),

                            ft.Text(
                                f"Raza: {cerda.raza}"
                            ),

                            ft.Text(
                                f"Color: {cerda.color}"
                            ),

                            ft.Text(
                                f"Edad: {cerda.edad} años"
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
                                f"Fecha registro: {cerda.fecha}"
                            ),

                        ]

                    )

                ),


                  
                    ft.Text(
                    "Resumen reproductivo",
                    size=20,
                    weight=ft.FontWeight.BOLD
                 ),


                
                ft.Row(

                    wrap=True,

                    spacing=15,

                    controls=[
                        



                        indicador(
                            "Servicios",
                            total_servicios
                        ),

                        indicador(
                            "Partos",
                            total_partos
                        ),

                        indicador(
                            "Destetes",
                            total_destetes
                        ),

                        indicador(
                            "Vivos",
                            lechones_vivos
                        ),

                        indicador(
                            "Muertos",
                            lechones_muertos
                        ),

                        indicador(
                            "Destetados",
                            lechones_destetados
                        ),

                    ]

                ),



                ft.Container(

                    padding=10,
                    width=300,
                    
                    
                    bgcolor="white",
                    
                    border_radius=12,
                                 
                    shadow=ft.BoxShadow(
                                 
                    blur_radius=10,
                                 
                    color="#D9D9D9",
                                 
                    offset=ft.Offset(0,3)
                                 
                    ),

                    content=ft.Column(

                        spacing=10,

                        controls=[


                        ft.Text(
                        "Últimos registros",
                         size=20,
                         weight=ft.FontWeight.BOLD
                        ),


                        ft.Row(
                            controls=[

                            ft.Text(
                             "Último servicio:",
                            width=170
                            ),

                            ft.Text(
                              ultimo_servicio.strftime("%Y-%m-%d")
                            if ultimo_servicio
                            else "Sin registros"
                            )

                            ]

                        ),


                        ft.Row(
                            controls=[

                             ft.Text(
                             "Último parto:",
                             width=170
                             ),

                            ft.Text(
                             ultimo_parto.strftime("%Y-%m-%d")
                             if ultimo_parto
                            else "Sin registros"
                            )

                             ]

                         ),


                         ft.Row(
                            controls=[

                              ft.Text(
                            "Último destete:",
                            width=170
                             ),

                            ft.Text(
                            ultimo_destete.strftime("%Y-%m-%d")
                            if ultimo_destete
                            else "Sin registros"
                            )

                            ]

                            ),



                        ft.Divider(),



                             ft.Text(
                             "Próximos eventos",
                             size=20,
                             weight=ft.FontWeight.BOLD
                             ),



                            ft.Row(
                                controls=[

                                    ft.Text(
                                        "Posible fecha de parto:",
                                        width=170
                                    ),

                                    ft.Text(
                                        posible_parto.strftime("%Y-%m-%d")
                                        if posible_parto
                                        else "Sin datos"
                                    )

                                ]

                            ),



                            ft.Row(
                                controls=[

                                    ft.Text(
                                        "Posible fecha de destete:",
                                        width=170
                                    ),

                                    ft.Text(
                                        posible_destete.strftime("%Y-%m-%d")
                                        if posible_destete
                                        else "Sin datos"
                                    )

                                ]

                            ),



                            ft.Row(
                                controls=[

                                    ft.Text(
                                        "Próximo servicio:",
                                        width=170
                                    ),

                                    ft.Text(
                                        proximo_servicio.strftime("%Y-%m-%d")
                                        if proximo_servicio
                                        else "Sin datos"
                                    )

                                ]

                            )

                  ]

                )
             ), 

                ft.ElevatedButton(

                    "Regresar",

                    icon=ft.Icons.ARROW_BACK,

                    bgcolor="#E8618C",

                    color="white",

                    on_click=lambda e: regresar()

                )


            ]

        )

    )
