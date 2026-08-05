from database.conexion import Conexion
from models.destete import Destete


class DesteteDAO:

    # ==========================
    # OBTENER TODOS LOS destetes
    # ==========================
    def obtener_todos(self):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT
            d.id_destete,
            d.id_cerda,
            c.arete,
            d.fecha_d,
            d.numle,
            d.peso
        FROM destetes d
        INNER JOIN cerdas c
            ON d.id_cerda = c.id
        ORDER BY d.id_destete;
        """

        cursor.execute(sql)

        registros = cursor.fetchall()

        destetes = []

        for registro in registros:

            destete = Destete(
                id_destete=registro[0],
                id_cerda=registro[1],
                fecha_d=registro[3],
                numle=registro[4],
                peso=registro[5]

                
            )

            # Solo para mostrar el arete en la tabla
            destete.arete = registro[2]

            destetes.append(destete)

        cursor.close()
        conexion.close()

        return destetes

    # ==========================
    # INSERTAR
    # ==========================
    def insertar(self, destete):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO destetes
        (id_cerda, fecha_d, numle, peso)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            sql,
            (
                destete.id_cerda,
                destete.fecha_d,
                destete.numle,
                destete.peso
                
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()

    # ==========================
    # ACTUALIZAR
    # ==========================
    def actualizar(self, destete):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE destetes
        SET
            id_cerda = %s,
            fecha_d = %s,
            numle = %s,
            peso = %s
        WHERE id_destete = %s
        """

        cursor.execute(
            sql,
            (
                destete.id_cerda,
                destete.fecha_d,
                destete.numle,
                destete.peso,
                destete.id_destete
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()

    # ==========================
    # ELIMINAR
    # ==========================
    def eliminar(self, id_destete):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM destetes WHERE id_destete = %s",
            (id_destete,)
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
            "SELECT COALESCE(MAX(id_destete), 0) FROM destetes"
        )

        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        return resultado[0]

     # ==========================
    # TOTAL DE DESTETES
    # ==========================
    def total_destetes(self, id_cerda):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT COUNT(*)
        FROM destetes
        WHERE id_cerda = %s
        """

        cursor.execute(sql, (id_cerda,))

        total = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return total


    # ==========================
    # TOTAL LECHONES DESTETADOS
    # ==========================
    def total_lechones_destetados(self, id_cerda):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT COALESCE(SUM(numle),0)
        FROM destetes
        WHERE id_cerda = %s
        """

        cursor.execute(sql, (id_cerda,))

        total = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return total


    # ==========================
    # ÚLTIMO DESTETE
    # ==========================
    def ultimo_destete(self, id_cerda):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT fecha_d
        FROM destetes
        WHERE id_cerda = %s
        ORDER BY fecha_d DESC
        LIMIT 1
        """

        cursor.execute(sql, (id_cerda,))

        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado:
            return resultado[0]

        return None