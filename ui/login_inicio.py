import flet as ft
import psycopg2

def login_view(page: ft.Page, sesion_usuario: dict = None):
    if sesion_usuario is None:
        sesion_usuario = {}

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

    status_text = ft.Text("", size=14)

    def login_clicked(e):
        if not correo_input.value or not password_input.value:
            status_text.value = "Por favor completa todos los campos"
            status_text.color = ft.Colors.RED
            page.update()
            return

        try:
            conexion = psycopg2.connect(
                dbname="porcilac",
                user="postgres",
                password="ale123",
                host="localhost",
                port="5432"
            )
            cursor = conexion.cursor()
            
            sql = '''
                SELECT u.correo, t.tipo 
                FROM usuarios u
                INNER JOIN tipo_usuario t ON u.tipo = t.id
                WHERE LOWER(u.correo) = %s AND u.password = %s
            '''
            
            correo_clean = correo_input.value.strip().lower()
            pass_clean = password_input.value.strip()

            cursor.execute(sql, (correo_clean, pass_clean))
            usuario = cursor.fetchone()
            
            cursor.close()
            conexion.close()

            if usuario:
                correo_db, nombre_rol = usuario
                
                # 📌 Guardamos en nuestro diccionario en memoria (cero errores)
                sesion_usuario["correo"] = correo_db
                sesion_usuario["rol"] = nombre_rol

                status_text.value = f"¡Bienvenido ({nombre_rol})!"
                status_text.color = ft.Colors.GREEN
                page.update()

                rol = str(nombre_rol).strip().lower()
                if "administrador" in rol or "admin" in rol:
                    page.go("/main_window")
                elif "empleado" in rol:
                    page.go("/empleado")
                else:
                    status_text.value = "Rol no asignado en el sistema."
                    status_text.color = ft.Colors.ORANGE
                    page.update()
            else:
                status_text.value = "Correo o contraseña incorrectos"
                status_text.color = ft.Colors.RED
                page.update()
            
        except Exception as ex:
            status_text.value = f"Error: {ex}"
            status_text.color = ft.Colors.RED
            page.update()

    btn_olvidaste = ft.TextButton(
        content=ft.Text("¿Olvidaste tu contraseña?", color=ft.Colors.BLUE_900),
        on_click=lambda _: page.go("/restablecer")
    )
    
    btn_iniciar = ft.ElevatedButton(
        content=ft.Text("Iniciar sesión", color=ft.Colors.WHITE),
        bgcolor=ft.Colors.PINK_ACCENT,
        width=380,
        height=45,
        on_click=login_clicked
    )

    header_section = ft.Column(
        [
            ft.Row([ft.Image(src="logo.png", height=85, fit="contain")], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(height=5)
        ],
        tight=True
    )

    form_fields = ft.Column(
        [
            correo_input,
            password_input,
            status_text,
            btn_iniciar,
            ft.Row([btn_olvidaste], alignment=ft.MainAxisAlignment.CENTER, width=380)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        tight=True,
        spacing=18,
    )

    form_card = ft.Container(
        content=ft.Column(
            [
                header_section,
                ft.Text("Iniciar sesión", size=24, weight=ft.FontWeight.BOLD),
                ft.Container(height=15),
                form_fields,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            tight=True,
        ),
        padding=35,
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        shadow=ft.BoxShadow(spread_radius=2, blur_radius=20, color=ft.Colors.BLACK12)
    )

    page.clean()
    page.add(
        ft.Stack(
            [
                ft.Image(src="fondo.png", fit="cover", expand=True, width=float("inf"), height=float("inf")),
                ft.Container(bgcolor="#B0BAC0", opacity=0.15, expand=True),
                ft.Column(
                    [
                        ft.Container(height=30),
                        ft.Row([form_card], alignment=ft.MainAxisAlignment.CENTER)
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