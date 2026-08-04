import flet as ft
from ui.restablecer_from import restablecer_form

def main(page: ft.Page):
    page.title = "PORCILAC - Restablecer Contraseña"
    restablecer_form(page)

if __name__ == "__main__":
    # El punto "." le dice a Flet que busque las imágenes en la carpeta actual
    ft.run(main, assets_dir="assets")
    