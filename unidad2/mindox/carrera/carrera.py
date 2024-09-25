from typing import List
from materias.materia import Materia
from estudiantes.estudiante import Estudiante
from semestres.semestre import Semestre


class Carrera:
    matricula: str
    nombre: str
    numero_semestres: int
    materias: list [Materia]
    estudiantes : list [Estudiante]
    semestres : list [Estudiante]
    
    
    