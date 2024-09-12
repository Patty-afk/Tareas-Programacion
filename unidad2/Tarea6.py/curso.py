class Curso:
    nombre_curso = ""
    codigo_curso = 0
    
    
    def __init__(self, nombre_curso, codigo_curso):
       self.codigo_curso = codigo_curso
       self.nombre_curso = nombre_curso
       
    def mostrar_info_curso(self):
       print("nombre del curso: ", self.nombre_curso) 
       print("codigo del curso: ", self.codigo_curso) 
    
    
    