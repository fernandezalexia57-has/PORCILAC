import flet as ft

from dao.usuario_dao import UsuarioDAO

def usuarios_table(regresar, editar_usuario, eliminar_usuario, nuevo_usuario=None):
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
    border_radius=12,  # 👈 Controla qué tan redondeadas están las esquinas (puedes ajustar entre 10 y 20)
    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,  # 👈 CRÍTICO: Recorta el fondo rosa en las esquinas redondeadas
    )

    mensaje = ft.Text()

    def abrir_dialogo_eliminar(e, usuario):
        def confirmar_eliminar(e_confirm):
            dialogo.open = False
            e.page.update()
            # Llamamos a la función eliminar pasándole el ID
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

        # Mostramos el diálogo en la página
        e.page.overlay.append(dialogo)
        dialogo.open = True
        e.page.update()

    def cargar_usuarios(e):
        try:
            usuario_dao = UsuarioDAO()
            usuarios = usuario_dao.obtener_todos()

            tabla.rows.clear()

            #Colocamos la informacion de un usuario dentro de la tabla
            for usuario in usuarios:
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
        except Exception as error:
            mensaje.value = f"Error al consultar usuarios: {error}"
            mensaje.color = ft.Colors.RED

    cargar_usuarios(e=None)

    return ft.Container(
        padding = 30,
        content = ft.Column(
            controls = [
                ft.Row(
                    controls = [
                        ft.Column(
                            controls = [
                                ft.Text(
                                    "Empleados registrados",
                                    size = 24,
                                    weight= ft.FontWeight.BOLD
                                ),
                                ft.Text(
                                    "Consulta de empleados",
                                    color = ft.Colors.PINK_400
                                )
                            ]
                        )
                    ],
                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN
                ),

                ft.Divider(),

                ft.Container(
                    content = tabla_redondeada,
                    border = ft.Border.all(
                        1,
                        ft.Colors.BLUE_GREY_200
                    ),
                    border_radius = 10,
                    padding = 10
                ),

                mensaje
            ],
            spacing =20,
            scroll = ft.ScrollMode.AUTO
        )
    )