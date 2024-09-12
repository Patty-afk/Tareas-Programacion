from curso import Curso

class Estudiante:
    nombre= ""
    edad = 0
    id_estudiante = ""
    curso = []
    
    def __init__(self,nombre, edad, id_estudiante):
        self.id_estudiante = id_estudiante
        self.edad = edad 
        self.nombre = nombre
        self.curso = []
        
    def agregar_curso(self, curso):
        self.curso.append(curso)
        
    
    def mostrar_informacion(self):
       print("Id de estudiante: ", self.id_estudiante)
       print("edad del estudiante: ", self.edad)
       print("Nombre del estudiante: ", self.nombre)
       
       
       print("----------------cursos del estudiante---------------- ")
       for Curso in self.curso:
           print("nombre del curso: ", Curso.nombre_curso)
           print("codigo del curso: ", Curso.codigo_curso)