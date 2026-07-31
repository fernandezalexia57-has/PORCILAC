class Destete:
    def __init__(self, id, arete, fecha, numLechones, pesoPromedio):
        self.id = id
        self.arete = arete
        self.fecha = fecha
        self.numLechones = numLechones
        self.pesoPromedio = pesoPromedio
        
    def mostrar_info(self):
        return f"Destete ID: {self.id}, Num Arete: {self.arete}, Fecha: {self.fecha}, Num Lechones: {self.numLechones}, Peso Promedio: {self.pesoPromedio}"