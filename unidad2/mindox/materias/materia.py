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
        
    def mostar_inform_materia(self):
        inform =f" \nid_materia: {self.id_materia}, nombre de la materia: {self.nombre_materia}, semestre: {self.semestre}, descripcion de la materia: {self.descripcion}, numero de creditos:{self.creditos}"    
        return inform  
        
        
        