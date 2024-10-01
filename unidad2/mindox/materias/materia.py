from datetime import datetime
from random import randint
from typing import List

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
        
    # def generar_numero_control(self):
    #     ultimos_dos_letras = self.nombre[-2:].upper()
    #     aleatorio = randint(1,1000)
    #     return f"MT{ultimos_dos_letras}{self.semestre}{self.creditos}{aleatorio}"
        
    def mostar_inform_materia(self):
        inform =f" \nid_materia: {self.id_materia}, nombre de la materia: {self.nombre_materia}, semestre: {self.semestre}, descripcion de la materia: {self.descripcion}, numero de creditos:{self.creditos}"    
        return inform  
        
        
        