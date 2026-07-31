class Servicio:
    
    # Metodo Constructor
    def __init__(self, id_servicio, id_cerda, fecha_s, tipo):
        self.id_servicio= id_servicio
        self.id_cerda = id_cerda
        self.fecha_s = fecha_s
        self.tipo = tipo
        
        
        
            
    def mostrar_info(self):
        return f"Preño ID: {self.id_servicio}, Cerda ID: {self.id_cerda}, fecha de preño: {self.fecha_s},  Tipo de preño: {self.tipo}"