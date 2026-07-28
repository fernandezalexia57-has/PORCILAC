class Destete:
    
    # Metodo Constructor
    def __init__(self, id, arete, fecha, numLechones, pesoPromedio):
        self.id= id
        self.arete = arete
        self.raza = fecha
        self.color = numLechones
        self.edad = pesoPromedio
        
            
    def mostrar_info(self):
        return f"Destete ID: {self.id}, Num Arete: {self.arete}, Fecha: {self.fecha},  Num Lechones: {self.numLechones}, Peso Promedio: {self.pesoPromedio}"