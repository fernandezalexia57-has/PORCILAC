import flet as ft
import psycopg2

def restablecer_form(page: ft.Page):
    page.padding = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    correo_input = ft.TextField(
        label="Correo electrónico",
        hint_text="ejemplo@gmail.com",
        width=380,
        border_radius=8,
        bgcolor=ft.Colors.WHITE
    )
    
    password_input = ft.TextField(
        label="Contraseña",
        hint_text="xxxxxxxxxx",
        password=True,
        can_reveal_password=True,
        width=380,
        border_radius=8,
        bgcolor=ft.Colors.WHITE
    )
    
    confirm_password_input = ft.TextField(
        label="Confirmar contraseña",
        hint_text="xxxxxxxxxx",
        password=True,
        can_reveal_password=True,
        width=380,
        border_radius=8,
        bgcolor=ft.Colors.WHITE
    )

    status_text = ft.Text("", size=14)

    def guardar_clicked(e):
        if not correo_input.value or not password_input.value:
            status_text.value = "Por favor completa todos los campos"
            status_text.color = ft.Colors.RED
            page.update()
            return

        if password_input.value != confirm_password_input.value:
            status_text.value = "Las contraseñas no coinciden"
            status_text.color = ft.Colors.RED
            page.update()
            return

        try:
            conexion = psycopg2.connect(
                dbname="porcilac",
                user="postgres",
                password="Wenferlo26",
                host="localhost",
                port="5432"
            )
            cursor = conexion.cursor()
            
            sql = 'INSERT INTO "restauraciones" ("correoElec", "nuevaPassword") VALUES (%s, %s)'
            cursor.execute(sql, (correo_input.value, password_input.value))
            
            conexion.commit()
            cursor.close()
            conexion.close()

            status_text.value = "¡Contraseña guardada con éxito!"
            status_text.color = ft.Colors.GREEN
            page.update()
            
        except Exception as ex:
            status_text.value = f"Error al guardar: {ex}"
            status_text.color = ft.Colors.RED
            page.update()

    btn_cancelar = ft.TextButton(
        content=ft.Text("Cancelar")
    )
    
    btn_guardar = ft.ElevatedButton(
        content=ft.Text("Guardar", color=ft.Colors.WHITE),
        bgcolor=ft.Colors.PINK_ACCENT,
        on_click=guardar_clicked
    )

    header_section = ft.Column(
        [
            ft.Row(
                [
                    ft.Image(
                        src="logo.png",
                        height=85,
                        fit="contain",
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Container(height=5)
        ],
        tight=True
    )

    form_fields = ft.Column(
        [
            correo_input,
            password_input,
            confirm_password_input,
            status_text,
            ft.Row(
                [btn_cancelar, btn_guardar],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                width=380
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        tight=True,
        spacing=18,
    )

    form_card = ft.Container(
        content=ft.Column(
            [
                header_section,
                ft.Text("Restablecer contraseña", size=24, weight=ft.FontWeight.BOLD),
                ft.Container(height=15),
                form_fields,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            tight=True,
        ),
        padding=35,
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=20,
            color=ft.Colors.BLACK12
        )
    )

    page.clean()
    page.add(
        ft.Stack(
            [
                ft.Image(
                    src="fondo.png",
                    fit="cover",
                    expand=True,
                    width=float("inf"),
                    height=float("inf"),
                ),
                ft.Container(
                    bgcolor="#B0BAC0",
                    opacity=0.15, 
                    expand=True,
                ),
                # Usamos una columna centrada con un pequeño espacio arriba para bajar el formulario
                ft.Column(
                    [
                        ft.Container(height=30), # <--- Esto empuja el formulario hacia abajo
                        ft.Row(
                            [form_card],
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True
                )
            ],
            expand=True
        )
    )
    page.update()