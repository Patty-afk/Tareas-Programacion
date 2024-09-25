from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint

class Escuela:
   lista_estudiantes: List[Estudiante] = []
   lista_grupos: List[Grupo] = []
   lista_maestros: List[Maestro] = []
   lista_materias: List[Materia] = []
   
   
   def registrar_estudiante(self, estudiante_regis: Estudiante):
      self.lista_estudiantes.append(estudiante_regis)
      
   def listar_estudiantes (self):
       print("** ESTUDIANTES **")
       for estudiante in self.lista_estudiantes:
         print(estudiante.mostrar_info_estudiante())
         
      
   def eliminar_estudiante(self, numero_control: str):
    for estudiante in self.lista_estudiantes: 
       if estudiante.numero_control == numero_control:
         self.lista_estudiantes.remove(estudiante)
         print ("estudiante eliminado")
         return
    print(f"No se encontro el estudiante con numero de control : {numero_control}")
            
         
   def generar_numero_control(self):
       ano = datetime.now().year
       mes = datetime.now().month
       longitud_mas_uno = len(self.lista_estudiantes) + 1
       aleatorio = randint(0,10000)
       numero_control = f"l{ano}{mes}{longitud_mas_uno}{aleatorio}"
       return numero_control
   
   
   
   
   
   def registrar_maestro(self, maestro_regis: Maestro):
      self.lista_maestros.append(maestro_regis)
      
   def listar_maestros (self):
      print ("**MAESTROS **")
      for maestro in self.lista_maestros:
         print(maestro.mostrar_infor_maestro())
         
   def eliminar_maestro(self, numero_control: str):
    for maestro in self.lista_maestros: 
       if maestro.numero_control == numero_control:
         self.lista_maestros.remove(maestro)
         print ("maestro eliminado")
         return
    print(f"No se encontro el maestro con numero de control : {numero_control}")
         
   def generar_numero_control_maestros(self, año: int, nombre: str, rfc: str):
      ano = año
      dia = datetime.now().day
      aleatorio = randint(500, 5000)
      letras_inicio = nombre [:2]
      letras_final = rfc [-2:]
      longitud_mas_uno = len(self.lista_estudiantes) + 1
      
      numero_control = f"M{ano}{dia}{aleatorio}{letras_inicio}{letras_final}{longitud_mas_uno}"
      return numero_control
   
   
   
      
   def registrar_materia(self, regis_materia:Materia):
      self.lista_materias.append(regis_materia)
      
   def listar_materias (self ):
      print("**MATERIAS**")
      for materias in self.lista_materias:
         print(materias.mostar_inform_materia())
         
   def eliminar_materia(self, id_materia: str):
    for materia in self.lista_materias: 
       if materia.id_materia ==id_materia:
         self.lista_materias.remove(materia)
         print ("materia eliminada")
         return
    print(f"No se encontro la materia con el id : {id_materia}")
      
   def generar_id_materia(self, nombre_materia:str, semestre:int, creditos:int):
      ult_digitos =nombre_materia [-2:].upper()
      random =randint(1,1000)
      
      id_materia = f"MT{ult_digitos}{semestre}{creditos}{random}"
      return id_materia
      