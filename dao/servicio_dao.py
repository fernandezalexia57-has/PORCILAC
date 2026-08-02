from database.conexion import Conexion
from models.servicio import Servicio


class ServicioDAO:

    # ==========================
    # OBTENER TODOS LOS SERVICIOS
    # ==========================
    def obtener_todos(self):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT
            s.id_servicio,
            s.id_cerda,
            c.arete,
            s.fecha_s,
            s.tipo
            
        FROM servicios s
        INNER JOIN cerdas c
            ON s.id_cerda = c.id
        ORDER BY s.id_servicio;
        """

        cursor.execute(sql)

        registros = cursor.fetchall()

        servicios = []

        for registro in registros:

            servicio = Servicio(
                id_servicio=registro[0],
                id_cerda=registro[1],
                fecha_s=registro[3],
                tipo=registro[4],
                
            )

            # Solo para mostrar el arete en la tabla
            servicio.arete = registro[2]

            servicios.append(servicio)

        cursor.close()
        conexion.close()

        return servicios

    # ==========================
    # INSERTAR
    # ==========================
    def insertar(self, servicio):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO servicios
        (id_cerda, fecha_s, tipo)
        VALUES (%s, %s, %s)
        """

        cursor.execute(
            sql,
            (
                servicio.id_cerda,
                servicio.fecha_s,
                servicio.tipo
                
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()

    # ==========================
    # ACTUALIZAR
    # ==========================
    def actualizar(self, servicio):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE servicios
        SET
            id_cerda = %s,
            fecha_s = %s,
            tipo = %s
        WHERE id_servicio = %s
        """

        cursor.execute(
            sql,
            (
                servicio.id_cerda,
                servicio.fecha_s,
                servicio.tipo,
                servicio.id_servicio
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()

    # ==========================
    # ELIMINAR
    # ==========================
    def eliminar(self, id_servicio):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM servicios WHERE id_servicio = %s",
            (id_servicio,)
        )

        conexion.commit()

        cursor.close()
        conexion.close()

    # ==========================
    # ÚLTIMO ID
    # ==========================
    def obtener_ultimo_id(self):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT COALESCE(MAX(id_servicio), 0) FROM servicios"
        )

        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        return resultado[0]


 # ==========================
    # TOTAL DE SERVICIOS
    # ==========================
    def total_servicios(self, id_cerda):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT COUNT(*)
        FROM servicios
        WHERE id_cerda = %s
        """

        cursor.execute(sql, (id_cerda,))

        total = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return total


    # ==========================
    # ÚLTIMO SERVICIO
    # ==========================
    def ultimo_servicio(self, id_cerda):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT fecha_s
        FROM servicios
        WHERE id_cerda = %s
        ORDER BY fecha_s DESC
        LIMIT 1
        """

        cursor.execute(sql, (id_cerda,))

        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado:
            return resultado[0]

        return None