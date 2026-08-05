import math

import flet as ft

from dao.usuario_dao import UsuarioDAO

def usuarios_list(nuevo_usuario, editar_usuario, eliminar_usuario):


    todos_usuarios = []
    usuarios_filtrados = []
    pagina_actual = {"valor": 1}
    ELEMENTOS_POR_PAGINA = 5

    paginacion = ft.Row(alignment=ft.MainAxisAlignment.CENTER, spacing=8)
    mensaje = ft.Text()

    def abrir_dialogo_eliminar(e, usuario):
            def confirmar_eliminar(e_confirm):
                dialogo.open = False
                e.page.update()
                eliminar_usuario(usuario.id)
    
            def cancelar_eliminar(e_cancel):
                dialogo.open = False
                e.page.update()
    
            dialogo = ft.AlertDialog(
                modal=True,
                title=ft.Text("Confirmar eliminación"),
                content=ft.Text(f"¿Estás seguro de que deseas eliminar a {usuario.nombre} {usuario.apellidoPaterno}?"),
                actions=[
                    ft.TextButton("Cancelar", on_click=cancelar_eliminar),
                    ft.ElevatedButton("Eliminar", color=ft.Colors.WHITE, bgcolor=ft.Colors.RED, on_click=confirmar_eliminar),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
    
            
            e.page.overlay.append(dialogo)
            dialogo.open = True
            e.page.update()

    tabla = ft.DataTable(
        heading_row_color=ft.Colors.PINK_200,
        heading_row_height=50,  
        column_spacing=30,
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Apellido Paterno")),
            ft.DataColumn(ft.Text("Apellido Materno")),
            ft.DataColumn(ft.Text("No. Empleado")),
            ft.DataColumn(ft.Text("Tipo")),
            ft.DataColumn(ft.Text("Correo electrónico")),
            ft.DataColumn(ft.Text("Contraseña")),
            ft.DataColumn(ft.Text("Editar")),
            ft.DataColumn(ft.Text("Eliminar"))
        ],
        rows=[]
    )

    tabla_redondeada = ft.Container(
    content=tabla,
    border_radius=12,  
    clip_behavior=ft.ClipBehavior.ANTI_ALIAS, 
    )


    def total_paginas():
        return max(1, math.ceil(len(usuarios_filtrados) / ELEMENTOS_POR_PAGINA))

    def cargar_tabla():
        tabla.rows.clear()
        
        # Calcular los índices según la página actual
        inicio = (pagina_actual["valor"] - 1) * ELEMENTOS_POR_PAGINA
        fin = inicio + ELEMENTOS_POR_PAGINA
        usuarios_pagina = usuarios_filtrados[inicio:fin]

            #Colocamos la informacion de un usuario dentro de la tabla
        for usuario in usuarios_pagina:
            tabla.rows.append(
                ft.DataRow(
                    cells = [
                        ft.DataCell(ft.Text(str(usuario.id))),
                        ft.DataCell(ft.Text(usuario.nombre)),
                        ft.DataCell(ft.Text(usuario.apellidoPaterno)),
                        ft.DataCell(ft.Text(usuario.apellidoMaterno)),
                        ft.DataCell(ft.Text(str(usuario.noEmpleado))),
                        ft.DataCell(ft.Text(usuario.tipo)),
                        ft.DataCell(ft.Text(usuario.correo)),
                        ft.DataCell(ft.Text(usuario.password)),
                        ft.DataCell(
                            ft.IconButton(
                                icon=ft.Icons.EDIT,
                                on_click=lambda e, u=usuario: editar_usuario(u)
                                ),
                        ),
                        ft.DataCell(
                            ft.IconButton(
                                icon=ft.Icons.DELETE,
                                on_click=lambda e, u=usuario: abrir_dialogo_eliminar(e, u)                           
                                )
                        ),
                    ]
                )
            )

    def cargar_paginacion():
        paginacion.controls.clear()

        # Botón Anterior
        paginacion.controls.append(
            ft.OutlinedButton(
                "Anterior",
                on_click=anterior,
                style=ft.ButtonStyle(
                    color=ft.Colors.BLACK,
                    side=ft.BorderSide(1, ft.Colors.BLACK)
                )
            )
        )

        # Botones de Números
        for i in range(1, total_paginas() + 1):
            es_activo = (i == pagina_actual["valor"])
            
            boton = ft.Container(
                width=35,
                height=35,
                border_radius=5,
                alignment=ft.Alignment(0, 0),
                bgcolor="#E85A8E" if es_activo else "white",
                border=ft.Border.all(1, "#E85A8E"),
                content=ft.Text(
                    str(i),
                    color="white" if es_activo else "black",
                    weight=ft.FontWeight.BOLD
                ),
                on_click=lambda e, pagina=i: cambiar_pagina(pagina)
            )
            paginacion.controls.append(boton)

        # Botón Siguiente
        paginacion.controls.append(
            ft.OutlinedButton(
                "Siguiente",
                on_click=siguiente,
                style=ft.ButtonStyle(
                    color=ft.Colors.BLACK,
                    side=ft.BorderSide(1, ft.Colors.BLACK)
                )
            )
        )

    def cambiar_pagina(pagina):
        pagina_actual["valor"] = pagina
        cargar_tabla()
        cargar_paginacion()
        paginacion.update()
        tabla_redondeada.update()

    def anterior(e):
        if pagina_actual["valor"] > 1:
            pagina_actual["valor"] -= 1
            cargar_tabla()
            cargar_paginacion()
            e.page.update()

    def siguiente(e):
        if pagina_actual["valor"] < total_paginas():
            pagina_actual["valor"] += 1
            cargar_tabla()
            cargar_paginacion()
            e.page.update()

    #Cargar la lista de usuarios desde la base de datos
    def cargar_usuarios():
        nonlocal todos_usuarios, usuarios_filtrados
        try:
            usuario_dao = UsuarioDAO()
            todos_usuarios = usuario_dao.obtener_todos()
            usuarios_filtrados = list(todos_usuarios) # Copia inicial
            pagina_actual["valor"] = 1
            
            cargar_tabla()
            cargar_paginacion()
        except Exception as error:
            mensaje.value = f"Error al consultar usuarios: {error}"
            mensaje.color = ft.Colors.RED

    #Buscador y filtro
    def buscar(e):
        texto = buscador.value.lower().strip()
        filtro_val = filtro.value
        usuarios_filtrados.clear()

        for p in todos_usuarios:
            coincide_texto = (
                texto in str(p.id).lower()
                or texto in str(p.nombre).lower()
                or texto in str(p.noEmpleado).lower()
            )
            
            coincide_filtro = True
            if filtro_val == "No. Empleado":
                coincide_filtro = texto in str(p.noEmpleado).lower()
            elif filtro_val == "Tipo":
                coincide_filtro = texto in str(p.tipo).lower()

            if coincide_texto and coincide_filtro:
                usuarios_filtrados.append(p)

        pagina_actual["valor"] = 1 # Reiniciar a la primera página tras buscar
        cargar_tabla()
        cargar_paginacion()
        e.page.update()

    buscador = ft.TextField(
        hint_text="Buscar (ID, Nombre, No. Empleado)",
        width=370,
        height=48,
        prefix_icon=ft.Icons.SEARCH,
        on_change=buscar #  Activa la búsqueda mientras escribes
    )

    filtro = ft.Dropdown(
        width=150,
        value="Todos",
        on_select=buscar,
        options=[
            ft.dropdown.Option("Todos"),
            ft.dropdown.Option("No. Empleado"),
            ft.dropdown.Option("Tipo"),
        ]
    )
    cargar_usuarios()  # Cargar usuarios al inicio

#Vista final
    return ft.Container(
        expand=True,
        bgcolor="#FFFFFF",
        padding=30,
        content=ft.Column(
            spacing=20,
            expand=True,
            controls=[
                # Título
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Empleados", size=32, weight=ft.FontWeight.BOLD)
                    ]
                ),
                # Barra superior (Buscador, Filtro, Botón Nuevo)
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=30,
                    controls=[
                        buscador,
                        filtro,
                        ft.ElevatedButton(
                            "+ Nuevo usuario",
                            height=48,
                            bgcolor="#E85A8E",
                            color="white",
                            on_click=lambda e: nuevo_usuario()
                        )
                    ]
                ),

                mensaje, # Para mostrar errores si los hay
                ft.Divider(),

                # Tabla envuelta en contenedor redondeado
                tabla_redondeada,

                # Paginación
                ft.Container(
                    height=60,
                    content=paginacion,
                    alignment=ft.Alignment(0, 0)
                )
            ]
        )
    )