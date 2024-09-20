from datetime import datetime


class Maestro: 
    numero_control :str
    nombre: str
    apellido :str
    rfc :str
    sueldo: float
    fecha_nacimiento_maestro: datetime
    
    def __init__(self, nombre:str, apellido:str, rfc:str, numero_control:str, sueldo:float):
        self.numero_control=numero_control 
        self.nombre =nombre
        self.apellido = apellido
        self.rfc =rfc
        self.sueldo =sueldo
        
        
    
