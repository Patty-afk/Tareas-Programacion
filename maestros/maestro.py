from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Maestro(Usuario):
    
    
    rfc: str
    sueldo: float
    
    def __init__ (self, numero_control, nombre: str, apellido: str, rfc: str, sueldo: float, contrasenia:str):
        #super significa la casa padre de usuario y sus atributos que comparte
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contrasenia=contrasenia, rol= Rol.MAESTRO)
        
        self.rfc = rfc
        self.sueldo = sueldo
        
        
        
        
    def mostrar_infor_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        infor= f" \nNumero de control: {self.numero_control}, nombre completo: {nombre_completo}, rfc: {self.rfc}, sueldo: {self.sueldo}, rol: {self.rol.value}"    
        return infor       

