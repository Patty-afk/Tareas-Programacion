from typing import List
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia

class Grupo:
    id: int
    estudiantes :list [Estudiante] = []
    maestro: list [Maestro] = []
    materias :list [Materia]= []
    tipo: chr