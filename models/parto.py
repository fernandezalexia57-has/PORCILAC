class Parto:
    
    # Metodo Constructor
    def __init__(self, id_parto, id_cerda, fecha, num_le, lechones_v, lechones_m, observaciones):
        self.id_parto= id_parto
        self.id_cerda = id_cerda
        self.fecha = fecha
        self.num_le = num_le
        self.lechones_v = lechones_v
        self.lechones_m = lechones_m
        self.observaciones = observaciones
        
        
    def mostrar_info(self):
        return f"Parto ID: {self.id_parto}, Cerda ID: {self.id_cerda}, fecha: {self.fecha},  Numero de Lechones: {self.num_le}, Lechones vivos: {self.lechones_v}, Lechones muertos: {self.lechones_m}, Observaciones: {self.observaciones}"