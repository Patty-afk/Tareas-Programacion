"""
- Pacientes
- Médicos
- Consultas
- Medicamentos
"""

from paciente import Paciente
from medico import Medico
from hospital import Hospital

hospital = Hospital()

paciente = Paciente("Juan", 2004, 76, 1.78, "Avenida Madero", 12) 
paciente_dos = Paciente("Jonathan", 2005, 70, 1.90, "Avenida Madero", 10 ) 

medico = Medico("Alberto", 1900, "ALB4817BNDDDF", "Av. Periodismo", 13) 
medico_dos = Medico("Maria", 1999, "MAU894FPF6GP", "Av lazaro cardenas", 14)


hospital.registrar_paciente(paciente=paciente)
hospital.registrar_paciente(paciente=paciente_dos)

eliminar_paciente_id = int(input("Ingresa id del paciente a eliminar: "))
hospital.eliminar_paciente(eliminar_paciente_id)

hospital.registrar_medico(medico=medico)
hospital.registrar_medico(medico =medico_dos)

eliminar_medicos_id = int(input("Ingresa id del medico a eliminar: "))
hospital.eliminar_medico(eliminar_medicos_id)


hospital.mostrar_pacientes()
hospital.mostrar_medicos()
hospital.mostrar_pacientes_mayores_edad()
hospital.mostrar_pacientes_menores_edad()


#hospital.registrar_consulta(id_paciente=1, id_medico=1)