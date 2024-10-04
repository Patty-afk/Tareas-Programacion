from usuario.usuario import Usuario
from usuario.utils.roles import Rol


class Coordinador(Usuario):
    sueldo:float
    rfc: str
    anios_antiguedad: int
    
    def __init__(self, sueldo:float, rfc: str, anios_antiguedad:int, rol: Rol, nombre:str, apellido:str, contrasenia: str, numero_control:str):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contrasenia=contrasenia, rol=Rol.COORDINADOR.value)
        
    
        self.sueldo = sueldo
        self.rfc = rfc
        self.anios_antiguedad = anios_antiguedad
         