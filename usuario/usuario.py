from utils.roles import Rol


class Usuario:
    numero_control: str
    nombre: str
    apellido:str
    contrasenia: str
    rol: Rol
    
    
    
    #clase padre que se usara en maestro y estudiante
    def __init__(self, numero_control: str, nombre:str, apellido:str, contrasenia:str, rol:Rol):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.contrasenia = contrasenia
        self.rol = rol
    
        pass