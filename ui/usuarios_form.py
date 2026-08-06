import flet as ft

from models.usuario import Usuario
from dao.usuario_dao import UsuarioDAO
from ui.usuarios_list import usuarios_list
<<<<<<< Updated upstream
    
=======
>>>>>>> Stashed changes

def usuario_form(regresar, usuario=None):
    editar = usuario is not None

    nombre_input = ft.TextField(
        label="Nombre: ",
        width = 400,
        value=usuario.nombre if editar else ""
    )

    apellido_paterno_input = ft.TextField(
        label="Apellido Paterno: ",
        width = 400,
        value=usuario.apellidoPaterno if editar else ""
    )

    apellido_materno_input = ft.TextField(
        label="Apellido Materno: ",
        width = 400,
        value=usuario.apellidoMaterno if editar else ""
    )

    no_empleado_input = ft.TextField(
        label="Número de Empleado: ",
        width = 400,
        value=str(usuario.noEmpleado) if editar else ""
    )

    tipo_texto = ft.Text(
        "Tipo de Usuario: ",
        size = 16
    )

    valor_tipo_inicial = str(usuario.tipo) if editar and usuario.tipo is not None else None

    valor_tipo = None
    if editar and usuario and usuario.tipo is not None:
        tipo_str = str(usuario.tipo).strip().lower() # Convertimos a texto minúsculo sin espacios
        
        if tipo_str in ["1", "administrador", "admin"]:
            valor_tipo = "1"
        elif tipo_str in ["2", "empl", "empleado"]:
            valor_tipo = "2"

    tipo_input = ft.RadioGroup(
        value=valor_tipo, 
        content=ft.Column(
            [
                ft.Radio(value="1", label="Administrador"),
                ft.Radio(value="2", label="Empleado"),
            ]
        )
    )

    correo_input = ft.TextField(
        label="Correo: ",
        width = 400,
        value=usuario.correo if editar else ""
    )

    password_input = ft.TextField(
        label="Contraseña: ",
<<<<<<< Updated upstream
        width = 400,
        password=True,
=======
        hint_text="xxxxxxxxxx",
        width = 400,
        password=True,
        can_reveal_password=True,
>>>>>>> Stashed changes
        value=usuario.password if editar else ""
    )

    mensaje = ft.Text(
        "",
        color = ft.Colors.GREEN
    )



    def guardar_usuario(e):
        #Recupera los valores de TexField
        nombre = nombre_input.value
        apellido_paterno = apellido_paterno_input.value
        apellido_materno = apellido_materno_input.value
        no_empleado = no_empleado_input.value
        tipo = tipo_input.value
        correo = correo_input.value
        password = password_input.value

        # Validación de campos vacíos
        if not nombre_input.value:
            mensaje.value = "Escriba el nombre del usuario"
            mensaje.color = ft.Colors.RED
            e.page.update()
            return

        if not apellido_paterno_input.value:
            mensaje.value = "Escriba el apellido paterno"
            mensaje.color = ft.Colors.RED
            e.page.update()
            return

        if not apellido_materno_input.value:
            mensaje.value = "Escriba el apellido materno"
            mensaje.color = ft.Colors.RED
            e.page.update()
            return

        if not no_empleado_input.value:
            mensaje.value = "Escriba el número de empleado"
            mensaje.color = ft.Colors.RED
            e.page.update()
            return

        if not no_empleado_input.value.isdigit():
            mensaje.value = "El número de empleado debe ser solo números"
            mensaje.color = ft.Colors.RED
            e.page.update()
            return

        if not tipo_input.value:
            mensaje.value = "Seleccione el tipo de usuario"
            mensaje.color = ft.Colors.RED
            e.page.update()
            return

        if not correo_input.value:
            mensaje.value = "Escriba el correo del usuario"
            mensaje.color = ft.Colors.RED
            e.page.update()
            return

        if not editar and not password_input.value:
            mensaje.value = "Escriba la contraseña del usuario"
            mensaje.color = ft.Colors.RED
            e.page.update()
            return

        try:
            usuario_dao = UsuarioDAO()

            if editar:
                guardar = Usuario(
                    id=usuario.id,
                    nombre=nombre,
                    apellidoPaterno=apellido_paterno,
                    apellidoMaterno=apellido_materno,
                    noEmpleado=int(no_empleado),
                    tipo=int(tipo),
                    correo=correo,
                    password=password
                )
                usuario_dao.actualizar(guardar)

<<<<<<< Updated upstream
=======
                # regresar(
                #     f"Usuario {nombre} actualizado correctamente"
                #             )
>>>>>>> Stashed changes

                e.page.snack_bar = ft.SnackBar(
                    content=ft.Text(f"Usuario {nombre} actualizado con éxito"),
                    bgcolor=ft.Colors.GREEN_700,
                    duration=3000
                )

            else:
                id_nuevo = usuario_dao.obtener_ultimo_id() + 1
                guardar = Usuario(
                    id=id_nuevo,
                    nombre=nombre,
                    apellidoPaterno=apellido_paterno,
                    apellidoMaterno=apellido_materno,
                    noEmpleado=int(no_empleado),
                    tipo=int(tipo),
                    correo=correo,
                    password=password
                )
                usuario_dao.insertar(guardar)

            e.page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Usuario {nombre} registrado con éxito"),
                bgcolor=ft.Colors.GREEN_700,
                duration=3000
            )
            e.page.snack_bar.open = True
            regresar()  
            
        except Exception as error:
            mensaje.value = f"Error al guardar el usuario: {error}"
            mensaje.color = ft.Colors.RED
            e.page.update()

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
    titulo_pantalla = "Editar usuario" if editar else "Registrar nuevo usuario"
    texto_boton = "Actualizar usuario" if editar else "Registrar usuario"
    icono_boton = ft.Icons.SAVE if editar else ft.Icons.ADD


    return ft.Container(
        padding = 30,
        content = ft.Column(
            controls = [
                ft.Text(
                    titulo_pantalla, 
                    size = 24,
                    weight = ft.FontWeight.BOLD
                ),

                ft.Text(
                    "Modifica los datos del usuario" if editar else "Captura los datos básicos del usuario",    
                    size = 14,
                    color = ft.Colors.PINK_400
                ),

                nombre_input,
                apellido_paterno_input,
                apellido_materno_input,
                no_empleado_input,
                tipo_texto,
                tipo_input,
                correo_input,
                password_input,

                ft.Row(
                    controls = [
                        ft.OutlinedButton(
                            "Cancelar",
                            icon=ft.Icons.CANCEL,
                            style=ft.ButtonStyle(
                            color=ft.Colors.BLACK,
                            side=ft.BorderSide(1, ft.Colors.BLACK)
                            ),
                            on_click = lambda e: regresar()
                        ),
                        ft.OutlinedButton(
                            texto_boton,
                            icon=icono_boton,
                            style=ft.ButtonStyle(
                            bgcolor="#E85A8E",
                            color=ft.Colors.WHITE
                            ),
                            on_click = guardar_usuario
                        )
                    ]
                ), 
                mensaje 
            ],
            spacing = 15 
        )
    )   