#DAO: Data Access Object
#libro_dao: Objeto de acceso a datos de la tabla libro

from database import conexion
from database.conexion import Conexion
from models.destete import Destete

class DesteteDAO:

    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        destetes = []
        try:
            with conexion.cursor() as cursor:
                cursor.execute('SELECT id, arete, fecha, "numLechones", "pesoPromedio" FROM destetes ORDER BY id ASC;')
                registros = cursor.fetchall()
                for reg in registros:
                    destete = Destete(
                        id=reg[0],
                        arete=reg[1],
                        fecha=reg[2],
                        numLechones=reg[3],
                        pesoPromedio=reg[4]
                    )
                    destetes.append(destete)
        except Exception as e:
            raise e
        finally:
            conexion.close()
        return destetes

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        ultimo_id = 0
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT MAX(id) FROM destetes;")
                resultado = cursor.fetchone()
                if resultado and resultado[0] is not None:
                    ultimo_id = resultado[0]
        except Exception as e:
            raise e
        finally:
            conexion.close()
        return ultimo_id

    def insertar(self, destete):
        conexion = Conexion.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                sql = """
                    INSERT INTO destetes (id, arete, fecha, "numLechones", "pesoPromedio")
                    VALUES (%s, %s, %s, %s, %s);
                """
                cursor.execute(sql, (
                    destete.id,
                    destete.arete,
                    destete.fecha,
                    destete.numLechones,
                    destete.pesoPromedio
                ))
                conexion.commit()
        except Exception as e:
            conexion.rollback()
            raise e
        finally:
            conexion.close()

    def actualizar(self, destete):
        conexion = Conexion.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                sql = """
                    UPDATE destetes 
                    SET arete = %s, fecha = %s, numLechones = %s, pesoPromedio = %s
                    WHERE id = %s;
                """
                cursor.execute(sql, (
                    destete.arete,
                    destete.fecha,
                    destete.numLechones,
                    destete.pesoPromedio,
                    destete.id
                ))
                conexion.commit()
        except Exception as e:
            conexion.rollback()
            raise e
        finally:
            conexion.close()

    def eliminar(self, id):
        conexion = Conexion.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                sql = "DELETE FROM destetes WHERE id = %s;"
                cursor.execute(sql, (id,))
                conexion.commit()
        except Exception as e:
            conexion.rollback()
            raise e
        finally:
            conexion.close()