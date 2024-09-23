from datetime import datetime

class Materia:
    id_materia: str
    nombre_materia: str
    semestre: int
    descripcion: str
    creditos: int
    
    
    def __init__ (self, id_materia:str, nombre_materia:str, semestre: int, descripcion:str, creditos:int):
        self.id_materia = id_materia
        self.nombre_materia = nombre_materia
        self.semestre = semestre
        self.descripcion = descripcion
        self.creditos = creditos
        
        
        