from typing import List
from materias.materia import Materia
from estudiantes.estudiante import Estudiante
from semestres.semestre import Semestre
from random import randint


class Carrera:
    matricula: str
    nombre: str
    numero_semestres: int 
    semestres : list [Semestre] = []
    
    def __init__(self, nombre:str, numero_semestres:int =0):
        self.id = self.generar_id_carrera(nombre)
        self.nombre = nombre
        self.numero_semestres = numero_semestres
        
    
    def generar_id_carrera(self, nombre: str):
        ult_digito = nombre[-2:].upper()
        random_num = randint(1, 10000)
        id_carrera = f"CR{ult_digito}{random_num}"
        return id_carrera
    
    def registar_semestre(self, semestre:Semestre):
        self.numero_semestres += 1
        self.semestres.append(semestre)
        
        
    def mostrar_info_carrera(self):
        info= f" \nMatricula: {self.id}, numero de semestres: {self.numero_semestres}, nombre: {self.nombre}"    
        return info  
        
    
    