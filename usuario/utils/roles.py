
#UN ENUM ES UNA CLASE QUE ALMACENA CONSTANTES, OSEA DATOS QUE NUNCA VAN A CAMBIAR
from enum import Enum


class Rol(Enum):
    ESTUDIANTE = "Estudiante"
    MAESTRO = "Maestro"
    COORDINADOR = "Coordinador"
    