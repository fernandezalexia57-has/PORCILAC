from database.conexion import Conexion  # O como lo tengas en tus otros DAOs

class ReportesDAO:
    def insertar(self, tipo, fecha_inicio, fecha_termino, cerdas_prenadas, partos_mes, lechones_destetados, mortalidad):
        conexion = Conexion.obtener_conexion() # Ajusta esto según cómo lo uses en tu proyecto
        try:
            with conexion.cursor() as cursor:
                sql = """
                    INSERT INTO reportes (tipo_reporte, fecha_inicio, fecha_termino, cerdas_preñadas, partos_mes, lechones_destetados, mortalidad)
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                """
                cursor.execute(sql, (tipo, fecha_inicio, fecha_termino, cerdas_prenadas, partos_mes, lechones_destetados, mortalidad))
                conexion.commit()
                return True
        except Exception as e:
            print("Error al insertar reporte:", e)
            return False
        finally:
            if conexion:
                conexion.close()