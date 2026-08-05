from database.conexion import Conexion
from models.parto import Parto


class PartoDAO:

    # ==========================
    # OBTENER TODOS LOS PARTOS
    # ==========================
    def obtener_todos(self):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT
            p.id_parto,
            p.id_cerda,
            c.arete,
            p.fecha,
            p.num_le,
            p.lechones_v,
            p.lechones_m,
            observaciones
        FROM partos p
        INNER JOIN cerdas c
            ON p.id_cerda = c.id
        ORDER BY p.id_parto;
        """

        cursor.execute(sql)

        registros = cursor.fetchall()

        partos = []

        for registro in registros:

            parto = Parto(
                id_parto=registro[0],
                id_cerda=registro[1],
                fecha=registro[3],
                num_le=registro[4],
                lechones_v=registro[5],
                lechones_m=registro[6],
                observaciones=registro[7]
                
            )

            # Solo para mostrar el arete en la tabla
            parto.arete = registro[2]

            partos.append(parto)

        cursor.close()
        conexion.close()

        return partos

    # ==========================
    # INSERTAR
    # ==========================
    def insertar(self, parto):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO partos
        (id_cerda, fecha, num_le, lechones_v, lechones_m, observaciones)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            sql,
            (
                parto.id_cerda,
                parto.fecha,
                parto.num_le,
                parto.lechones_v,
                parto.lechones_m,
                parto.observaciones
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()

    # ==========================
    # ACTUALIZAR
    # ==========================
    def actualizar(self, parto):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE partos
        SET
            id_cerda = %s,
            fecha = %s,
            num_le = %s,
            lechones_v = %s,
            lechones_m = %s,
            observaciones = %s
        WHERE id_parto = %s
        """

        cursor.execute(
            sql,
            (
                parto.id_cerda,
                parto.fecha,
                parto.num_le,
                parto.lechones_v,
                parto.lechones_m,
                parto.observaciones,
                parto.id_parto
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()

    # ==========================
    # ELIMINAR
    # ==========================
    def eliminar(self, id_parto):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM partos WHERE id_parto = %s",
            (id_parto,)
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
            "SELECT COALESCE(MAX(id_parto), 0) FROM partos"
        )

        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        return resultado[0]

     # ==========================
    # TOTAL DE PARTOS
    # ==========================
    def total_partos(self, id_cerda):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT COUNT(*)
        FROM partos
        WHERE id_cerda = %s
        """

        cursor.execute(sql, (id_cerda,))

        total = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return total


    # ==========================
    # TOTAL LECHONES VIVOS
    # ==========================
    def total_lechones_vivos(self, id_cerda):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT COALESCE(SUM(lechones_v),0)
        FROM partos
        WHERE id_cerda = %s
        """

        cursor.execute(sql, (id_cerda,))

        total = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return total


    # ==========================
    # TOTAL LECHONES MUERTOS
    # ==========================
    def total_lechones_muertos(self, id_cerda):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT COALESCE(SUM(lechones_m),0)
        FROM partos
        WHERE id_cerda = %s
        """

        cursor.execute(sql, (id_cerda,))

        total = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return total


    # ==========================
    # ÚLTIMO PARTO
    # ==========================
    def ultimo_parto(self, id_cerda):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT fecha
        FROM partos
        WHERE id_cerda = %s
        ORDER BY fecha DESC
        LIMIT 1
        """

        cursor.execute(sql, (id_cerda,))

        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado:
            return resultado[0]

        return None
    
    # ==========================
    # LECHONES VIVOS DEL ÚLTIMO PARTO
    # ==========================
    def ultimo_lechones_vivos(self, id_cerda):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT lechones_v
        FROM partos
        WHERE id_cerda = %s
        ORDER BY fecha DESC
        LIMIT 1
        """

        cursor.execute(sql, (id_cerda,))

        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado:
            return resultado[0]

        return 0