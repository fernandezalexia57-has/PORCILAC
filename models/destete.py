class Destete:
    
    # Metodo Constructor
    def __init__(self, id_destete, id_cerda, fecha_d, numle, peso):
        self.id_destete= id_destete
        self.id_cerda = id_cerda
        self.fecha_d = fecha_d
        self.numle = numle
        self.peso = peso
        
        
        
        
            
    def mostrar_info(self):
        return f"Destete ID: {self.id_destete}, Cerda ID: {self.id_cerda}, fecha de destete: {self.fecha_d},  Numero de lechones: {self.numle},  Peso promedio: {self.peso}"