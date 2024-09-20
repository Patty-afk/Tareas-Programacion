
from typing import List
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint
from estudiantes.estudiante import Estudiante


class Escuela:
    lista_estudiantes: list[Estudiante] = []
    lista_maestros: list[Maestro] = []
    lista_grupos: list[Grupo] = []
    lista_materias : list[Materia] = []
    
    
    #append agregar algo al final de la lista
    #self. agregar algo a la lista
    def registar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
    
    def generar_numero_control_estudiante(self):
        ano = datetime.now().year
        mes = datetime.now().month
        longitud_mas_uno = len(self.lista_estudiantes) + 1
        aleatorio = randint(0,10000)
        numero_control_estudiante = f"l{ano}{mes}{longitud_mas_uno}{aleatorio}"
        return numero_control_estudiante
    
    
    def registrar_maestro(self, maestro:Maestro):
        self.lista_maestros.append(maestro)
        
    def generar_numero_control_maestro(self):
        ano_nacimiento = ano_nacimiento
        dia =datetime.now().day
        numero_aleatorio = randint(500,5000)
        nombre_inicio = nombre_inicio [:2].upper()
        rfc_final = rfc_final [-2:].upper()
        long_mas_uno = len(self.lista_maestros) + 1
        
        numero_control_maestro= f"M{ano_nacimiento}{dia}{numero_aleatorio}{nombre_inicio}{rfc_final}{long_mas_uno}"
        return numero_control_maestro