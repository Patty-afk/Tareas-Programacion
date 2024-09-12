from estudiantes import Estudiante
from curso import Curso


estudiantes = Estudiante


curso1 = Curso("calculo diferencial", 109)
curso2 = Curso("calculo vectorial", 102)
curso3 = Curso("programacion avanzada", 106)

estudiante_uno = Estudiante("Ana Maria Rubio Alejo", 19, 21129081)
estudiante_dos = Estudiante("Victoria Garcia Hernandez", 20, 21268495)
estudiante_tres = Estudiante("Miroslava Zavala Aguilar", 18, 24046935)

estudiante_uno.agregar_curso(curso1)
estudiante_dos.agregar_curso(curso2)
estudiante_tres.agregar_curso(curso3)

print("----------Información del estudiante 1--------")
estudiante_uno.mostrar_informacion()
print("********************************")


print("-----------Información del estudiante 2-----------")
estudiante_dos.mostrar_informacion()
print("********************************")


print("------------Información del estudiante 3-----------")
estudiante_tres.mostrar_informacion()
print("********************************")