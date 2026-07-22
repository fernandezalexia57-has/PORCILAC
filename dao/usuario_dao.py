#DAO: Data Access Object
#libro_dao: Objeto de acceso a datos de la tabla libro

from database import conexion
from database.conexion import Conexion
from models.usuario import Usuario

class UsuarioDAO:

    #SELECT * from usuario
    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM vista_usuarios" )
        registros = cursor.fetchall()

        usuarios = []
        for reg in registros:
            usuario = Usuario(
                id=reg[0],
                nombre=reg[1],
                apellidoPaterno=reg[2],
                apellidoMaterno=reg[3],
                noEmpleado=reg[4],
                tipo=reg[5],
                correo=reg[6],
                password=reg[7])
            usuarios.append(usuario)
        cursor.close()
        conexion.close()
        return usuarios
    
    def insertar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql="""
        INSERT INTO usuarios (id, nombre, apellidoPaterno, apellidoMaterno, noEmpleado, tipo, correo, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql,
                       (usuario.id,
                        usuario.nombre,
                        usuario.apellidoPaterno,
                        usuario.apellidoMaterno,
                        usuario.noEmpleado,
                        usuario.tipo,
                        usuario.correo,
                        usuario.password))
        
        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql="""
        UPDATE usuarios
        SET nombre = %s,
        apellidoPaterno = %s, 
        apellidoMaterno = %s,
        noEmpleado = %s,
        tipo = %s,
        correo = %s,
        password = %s
        WHERE id= %s
        """
        cursor.execute(sql,
                        (usuario.nombre,
                         usuario.apellidoPaterno,
                         usuario.apellidoMaterno,
                         usuario.noEmpleado,
                         usuario.tipo,
                         usuario.correo,
                         usuario.password,
                         usuario.id))
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, usuario_id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM usuarios WHERE id = %s", 
            (usuario_id,)
            )
        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT id FROM usuarios ORDER BY id DESC")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado is None:
            return 0
        return resultado[0]