class Cerda:
    
    # Metodo Constructor
    def __init__(self, id, arete, raza, color, edad, estado,fecha):
        self.id= id
        self.arete = arete
        self.raza = raza
        self.color = color
        self.edad = edad
        self.estado = estado
        self.fecha = fecha
        self.color = color
        
        
            
    def mostrar_info(self):
        return f"Cerda ID: {self.id}, Num. Arete: {self.arete}, Raza: {self.raza},  Color: {self.color}, Edad: {self.edad}, Estado: {self.estado}, Fecha de registro: {self.fecha}"