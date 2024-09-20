
from typing import  List
from paciente.paciente import Paciente
from medico.medico import Medico
    
    
class ValidadorHospital:
    def validar_existencia_paciente(self, id_paciente: int, lista_pacientes:List(Paciente)):
        for paciente in lista_pacientes:
              if paciente.id == id_paciente:
                return True
  
        return False
    
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
            
        return False
        
    def validar_cantidad_usuarios(self, lista_pacientes: list(Paciente), lista_medicos: list(Medico)):
        if len(self.pacientes) == 0:
            print("No puedes registra una consulta, no existen pacientes")
            return False
        