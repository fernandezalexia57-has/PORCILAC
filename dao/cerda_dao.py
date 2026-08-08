from database import conexion
from database.conexion import Conexion
from models.cerda import Cerda

class CerdaDAO:

    #SELECT * from cerda
    def obtener_todos(self):
      conexion = Conexion.obtener_conexion()
      cursor = conexion.cursor()

      cursor.execute("SELECT * FROM cerdas")
      registros = cursor.fetchall()

      cerdas = []

      for registro in registros:
        cerda = Cerda(
            id=registro[0],
            arete=registro[1],
            raza=registro[2],
            color= registro[3],
            edad=registro[4],
            estado=registro[5],
            fecha=registro[6]

        )
        cerdas.append(cerda)

      cursor.close()
      conexion.close()

      return cerdas

    def insertar(self, cerda):
     conexion = Conexion.obtener_conexion()
     cursor = conexion.cursor()

     sql = """
     INSERT INTO cerdas
      (arete, raza, color, edad, estado, fecha)
     VALUES (%s, %s, %s, %s, %s, %s)
     """

     cursor.execute(
        sql,
        (
            cerda.arete,
            cerda.raza,
            cerda.color,
            cerda.edad,
            cerda.estado,
            cerda.fecha
        )
     )

     conexion.commit()

     cursor.close()
     conexion.close()
     
     
    def existe_arete(self, arete):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = "SELECT COUNT(*) FROM cerdas WHERE arete = %s"

        cursor.execute(sql, (arete,))

        existe = cursor.fetchone()[0] > 0

        cursor.close()
        conexion.close()

        return existe
        
        
    def actualizar(self, cerda):
     conexion = Conexion.obtener_conexion()
     cursor = conexion.cursor()

     sql = """
     UPDATE cerdas
     SET
        arete = %s,
        raza = %s,
        color = %s,
        edad = %s,
        estado = %s,
        fecha = %s
        
     WHERE id = %s
     """

     cursor.execute(
        sql,
        (
            cerda.arete,
            cerda.raza,
            cerda.color,
            cerda.edad,
            cerda.estado,
            cerda.fecha,
            cerda.id
        )
     )

     conexion.commit()

     cursor.close()
     conexion.close()

    def eliminar(self, id):
     conexion = Conexion.obtener_conexion()
     cursor = conexion.cursor()

     cursor.execute(
        "DELETE FROM cerdas WHERE id = %s",
        (id,)
     )

     conexion.commit()

     cursor.close()
     conexion.close()
    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT id FROM cerdas ORDER BY id DESC")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado is None:
            return 0
        return resultado[0]
    
    def actualizar_estado(self, id_cerda, estado):

     conexion = Conexion.obtener_conexion()
     cursor = conexion.cursor()

     sql = """
     UPDATE cerdas
     SET estado = %s
     WHERE id = %s
     """

     cursor.execute(
        sql,
        (
            estado,
            id_cerda
        )
     )

     conexion.commit()

     cursor.close()
     conexion.close()
     
    def obtener_estado(self, id_cerda):

     conexion = Conexion.obtener_conexion()
     cursor = conexion.cursor()

     cursor.execute(
        "SELECT estado FROM cerdas WHERE id=%s",
        (id_cerda,)
     )

     resultado = cursor.fetchone()

     cursor.close()
     conexion.close()

     if resultado:
        return resultado[0]

     return None
 
    def obtener_por_id(self, cerda_id):

     conexion = Conexion.obtener_conexion()
     cursor = conexion.cursor()

     cursor.execute(
        "SELECT * FROM cerdas WHERE id = %s",
        (cerda_id,)
     )

     resultado = cursor.fetchone()

     cursor.close()
     conexion.close()

     if resultado:
        return Cerda(
            id=resultado[0],
            arete=resultado[1],
            raza=resultado[2],
            color=resultado[3],
            edad=resultado[4],
            estado=resultado[5],
            fecha=resultado[6]
        )

     return None
 
    def dar_baja(self, id):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE cerdas
        SET estado = 'Baja'
        WHERE id = %s
        """

        cursor.execute(sql, (id,))

        conexion.commit()

        cursor.close()
        conexion.close()