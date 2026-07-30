import flet as ft 
from models.usuario import Usuario
from dao.usuario_dao import UsuarioDAO

def usuarios_form(regresar):
    nombre_input = ft.TextField(
        label="Nombre",
        width=400
    )
    
    apellido_paterno_input = ft.TextField(
        label="Apellido Paterno",
        width=400
    )

    apellido_materno_input = ft.TextField(
        label="Apellido Materno",
        width=400
    )

    no_empleado_input = ft.TextField(
        label="Número de Empleado",
        width=400
    )

    tipo_input = ft.Dropdown(
        label="Tipo de Usuario",
        width=400,
        options=[
            ft.dropdown.Option("Administrador"),
            ft.dropdown.Option("Empleado")
        ]
    )

    correo_input = ft.TextField(
        label="Correo electrónico",
        width=400
    )

    password_input = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=400
    )
    
    mensaje = ft.Text(
        "",
        color=ft.Colors.GREEN
    )
    
    def guardar_usuario(e):
        nombre = nombre_input.value
        apellido_paterno = apellido_paterno_input.value
        apellido_materno = apellido_materno_input.value
        no_empleado = no_empleado_input.value
        tipo = tipo_input.value
        correo = correo_input.value
        password = password_input.value
         
        if not nombre or not apellido_paterno or not no_empleado or not tipo or not correo or not password:
            mensaje.value = "Todos los campos obligatorios deben llenarse"
            mensaje.color = ft.Colors.RED
            e.page.update()
            return 
        
        try:
            usuario_dao = UsuarioDAO()
            id = usuario_dao.obtener_ultimo_id() + 1 if hasattr(usuario_dao, 'obtener_ultimo_id') else 1
            
            nuevo_usuario = Usuario(
                id=id,
                nombre=nombre,
                apellidoPaterno=apellido_paterno,
                apellidoMaterno=apellido_materno,
                noEmpleado=no_empleado,
                tipo=tipo,
                correo=correo,
                password=password
            )
            
            usuario_dao.insertar(nuevo_usuario)
            
            mensaje.value = f"El empleado '{nombre}' ha sido registrado exitosamente"
            mensaje.color = ft.Colors.GREEN
            
            # Limpiar campos
            nombre_input.value = ""
            apellido_paterno_input.value = ""
            apellido_materno_input.value = ""
            no_empleado_input.value = ""
            tipo_input.value = None
            correo_input.value = ""
            password_input.value = ""
            
        except Exception as error:
            mensaje.value = f"Error al insertar el usuario: {error}"
            mensaje.color = ft.Colors.RED
            
        e.page.update()
            
    return ft.Container(
        padding=30,
        content=ft.Column(
            controls=[
                ft.Text(
                    "Registro de nuevo empleado",
                    size=24,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Text(
                    "Capture los datos del empleado",
                    size=14,
                    color=ft.Colors.BLACK_87
                ),
                nombre_input,
                apellido_paterno_input,
                apellido_materno_input,
                no_empleado_input,
                tipo_input,
                correo_input,
                password_input,
                ft.Row(  
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
                            "Registrar empleado",
                            icon=ft.Icons.ADD,
                            style=ft.ButtonStyle(
                                bgcolor="#E85A8E",
                                color=ft.Colors.WHITE
                            ),
                            on_click=guardar_usuario
                        )
                    ],
                ),
                mensaje
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO
        )
    )