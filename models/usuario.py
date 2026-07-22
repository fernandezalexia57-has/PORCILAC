class Usuario:

    # Constructor
    def __init__(self, id, nombre, apellidoPaterno, apellidoMaterno, noEmpleado,tipo, correo, password):
        self.id = id
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.noEmpleado = noEmpleado
        self.tipo = tipo
        self.correo = correo
        self.password = password

        def activar(self):
            self.activo = True
            

        def desactivar(self):
            self.activo = False

        def mostrar_info(self):
            return f"Usuario ID: {self.id}, Nombre: {self.nombre}, Apellido Paterno: {self.apellidoPaterno}, Apellido Materno: {self.apellidoMaterno}, Numero de Empleado: {self.noEmpleado}, Tipo: {self.tipo}, Correo: {self.correo}, Contraseña: {self.password} "