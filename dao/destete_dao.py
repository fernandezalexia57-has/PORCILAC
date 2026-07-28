# DAO: Data Access Object 
# libro_dao: Objeto de acceso a datos de la tabla libro

from database import conexion
from database.conexion import Conexion
from models.destete import Destete

class DesteteDAO:
    
    #SELECT * from destete
    def obtener_todos(self):
      conexion = Conexion.obtener_conexion()
      cursor = conexion.cursor()

      cursor.execute("SELECT * FROM destete")
      registros = cursor.fetchall()

      destetes = []

      for registro in registros:
        destete = Destete(
            id=registro[0],
            arete=registro[1],
            fecha= registro[3],
            numlechones=registro[3],
            pesoPromedio=registro[4]
            
        )
        destetes.append(destete)

      cursor.close()
      conexion.close()

      return destetes
    
    def insertar(self, destete):
     conexion = Conexion.obtener_conexion()
     cursor = conexion.cursor()

     sql = """
     INSERT INTO cerdas
      (arete, fecha, num_Lechones, peso_Promedio)
     VALUES (%s, %s, %s, %s)
     """

     cursor.execute(
        sql,
        (
            destete.arete,
            destete.fecha,
            destete.numLechones,
            destete.pesoPromedio
        )
     )

     conexion.commit()

     cursor.close()
     conexion.close()
        
        
    def actualizar(self, destete):
     conexion = Conexion.obtener_conexion()
     cursor = conexion.cursor()

     sql = """
     UPDATE destetes
     SET
        arete = %s,
        fecha= %s,
        numLechones = %s,
        pesoPromedio= %s

        
     WHERE id = %s
     """

     cursor.execute(
        sql,
        (
            destete.arete,
            destete.fecha,
            destete.numLechones,
            destete.pesoPromedio
        )
     )

     conexion.commit()

     cursor.close()
     conexion.close()
        
    def eliminar(self, id):
     conexion = Conexion.obtener_conexion()
     cursor = conexion.cursor()

     cursor.execute(
        "DELETE FROM destetes WHERE id = %s",
        (id,)
     )

     conexion.commit()
     cursor.close()
     conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT id FROM destetes ORDER BY id DESC")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado is None:
            return 0
        return resultado[0]