from typing import List
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from random import randint

class Grupo:
    id: str
    estudiantes: List[Estudiante] = []
    maestros: List[Maestro] = []
    materias: List[Materia] = []
    tipo: chr
    id_semestre: str
    
    
    def __init__(self, tipo:chr, id_semestre:str):
        self.id = self.generar_id(tipo)
        self.tipo = tipo
        self.id_semestre = id_semestre
        
        
    def generar_id(self, tipo:chr) -> str:
        return f"{tipo}-{randint(0, 1000000)}-{randint(0,100000)}"
    
    def mostrar_info_grupos(self):
        info= f" \n ID: {self.id}, tipo de salon: {self.tipo}, id del semestre: {self.id_semestre}"    
        return info