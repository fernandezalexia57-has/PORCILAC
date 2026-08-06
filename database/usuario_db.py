from database.conexion import obtener_conexion 

def actualizar_contrasena(correo, nueva_password):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()

        # 1. Verificar si el correo existe
        cursor.execute("SELECT id_usuario FROM usuario WHERE correo = %s;", (correo,))
        usuarios = cursor.fetchall()

        if not usuarios:
            cursor.close()
            conn.close()
            return False, "El correo electrónico no está registrado."

        # 2. Hacer el UPDATE de la contraseña
        cursor.execute(
            "UPDATE usuario SET password = %s WHERE correo = %s;",
            (nueva_password, correo)
        )
        conn.commit()

        cursor.close()
        conn.close()
        return True, "¡Contraseña actualizada con éxito!"

    except Exception as e:
        return False, f"Error al actualizar la contraseña: {e}"