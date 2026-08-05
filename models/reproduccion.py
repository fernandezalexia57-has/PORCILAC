class Reproduccion:

    # Constructor
    def __init__(self, id, numArete, fecha_reproduccion, tipo):
        self.id = id
        self.numArete = numArete
        self.fecha_reproduccion = fecha_reproduccion
        self.tipo = tipo

        def activar(self):
            self.activo = True
            

        def desactivar(self):
            self.activo = False

        def mostrar_info(self):
            return f"Reproducción ID: {self.id}, Número de Arete: {self.numArete}, Fecha: {self.fecha_reproduccion}, Tipo: {self.tipo} "