from typing import List
from medico.medico import Medico
from paciente.paciente import Paciente
from Consulta.consulta import Consulta


class Hospital:
    pacientes : List[Paciente] = []
    medicos : list[Medico] = []
    consultas : list[Consulta] = []


    def registrar_consulta(self, id_paciente, id_medico):
        if not self.validar_cantidad_usuarios() == False:
            return
        
        if self.validar_existencia_paciente(id_paciente) == False or self.validar_existencia_medico(id_medico) == False:
            print("No se puede registrar la consulta, no existe el médico o el paciente")
            return
        print("Continuamos con el registro")

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)
        
    def eliminar_paciente(self, id):
        for pacientes in self.pacientes:
            if pacientes.id == id :
                self.pacientes.remove(pacientes)
                print("eliminaste con exito paciente")
                return
        print("se elimino paciente correctamente")

    def registrar_medico(self, medico):
        self.medicos.append(medico)
        
    def eliminar_medico(self, id):
        for medicos in self.medicos:
            if medicos.id == id :
                self.medicos.remove(medicos)
                return
        print("eliminaste con exito medico ")
        

    def mostrar_pacientes(self):
        print("-/-/-Pacientes en el Sistema-/-/-")
        if len(self.pacientes) ==0:
            print("no esta registrado ningun paciente")
        for paciente in self.pacientes:
            paciente.mostrar_informacion()

            
    def mostrar_pacientes_menores_edad (self):
         print("-/-/-/Pacientes menores de edad -/-/-")
         for pacientes in self.pacientes:
             if pacientes.ano_nacimiento > 2006: 
                pacientes.mostrar_informacion()
                
             
    def mostrar_pacientes_mayores_edad (self):
        print("-/-/- Pancientes mayores de edad en el sistema -/-/-")
        for pacientes in self.pacientes:
            if pacientes.ano_nacimiento <=2006: 
                pacientes.mostrar_informacion()

        
    def mostrar_medicos(self):
        print("-/-/- Medicos en el Sistema -/-/-")
        for medico in self.medicos:
            medico.mostrar_informacion()
    

    def validar_existencia_paciente(self, id_paciente):
        for paciente in self.pacientes:
              if paciente.id == id_paciente:
                return True
  
        return False
    
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
            
        return False
        
    def validar_cantidad_usuarios(self):
        if len(self.pacientes) == 0:
            print("No puedes registra una consulta, no existen pacientes")
            return False
        
        if len(self.medicos) == 0:
            print("No puedes registra una consulta, no existen médicos")
            return False
        
        return True

    
        