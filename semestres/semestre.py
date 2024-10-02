from typing import List
from materias.materia import Materia
from grupos.grupo import Grupo
from random import randint


class Semestre:
    id: str
    numero: int
    materias: list [Materia]
    grupos : list [Grupo]
    id_carrera: str
    
    def __init__(self, numero: int, id_carrera:str):
        self.id = self.generar_id(numero)
        self.id_carrera = id_carrera
        self.numero = numero
        self.grupos = []
        
        
    def  generar_id(self, numero_semestre:int) -> str:
        return f"{numero_semestre}-{randint(0,100000)}-{randint(0, 100000)}"
    
    def registar_grupo_en_semestre(self, grupo: Grupo):
        self.grupos.append(grupo)
        
    def mostrar_info_semestres(self):
        info= f" \n ID: {self.id}, numero: {self.numero} ID carrera: {self.id_carrera}"    
        return info 