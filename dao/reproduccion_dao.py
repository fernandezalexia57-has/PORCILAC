#DAO: Data Access Object
#libro_dao: Objeto de acceso a datos de la tabla libro

from database import conexion
from database.conexion import Conexion
from models.reproduccion import Reproduccion

class ReproduccionDAO:

    #SELECT * from reproduccion
    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM vista_reproduccion" )
        registros = cursor.fetchall()

        reproducciones = []
        for reg in registros:
            reproduccion = Reproduccion(
                id=reg[0],
                numArete=reg[1],
                fecha_reproduccion=reg[2],
                tipo=reg[3])
            reproducciones.append(reproduccion)
        cursor.close()
        conexion.close()
        return reproducciones

    def insertar(self, reproduccion):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql="""
        INSERT INTO reproduccion (id, num_arete, fecha_reproduccion, tipo)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql,
                       (reproduccion.id,
                        reproduccion.numArete,
                        reproduccion.fecha_reproduccion,
                        reproduccion.tipo))
        
        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, reproduccion):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql="""
        UPDATE reproduccion
        SET num_arete = %s,
        fecha_reproduccion = %s,
        tipo = %s
        WHERE id = %s
        """
        cursor.execute(sql,
                        (reproduccion.numArete,
                         reproduccion.fecha_reproduccion,
                         reproduccion.tipo,
                         reproduccion.id))
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, reproduccion_id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM reproduccion WHERE id = %s", 
            (reproduccion_id,)
            )
        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT id FROM reproduccion ORDER BY id DESC")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado is None:
            return 0
        return resultado[0]