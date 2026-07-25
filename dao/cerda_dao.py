# DAO: Data Access Object 
# libro_dao: Objeto de acceso a datos de la tabla libro

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