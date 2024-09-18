"""
- Pacientes
- Médicos
- Consultas
- Medicamentos
"""

from paciente.paciente import Paciente
from medico.medico import Medico
from hospital.hospital import Hospital

hospital = Hospital()

while True:
    print("****Bienvenido al sistema de hospital****")
    print("1. Registrar paciente")
    print("2. registar medico")
    print("3. mostrar paciente")
    print("4. mostrar medicos")
    print("5. Eliminar pacientes")
    print("6. Eliminar medicos")
    print("7. Mostrar pacientes menores de edad")
    print("8. Mostrar pacientes mayores de edad")
    print("9. salir")
    
    opcion_usuario = input("selecciona la opcion deseada: ")
    if opcion_usuario == "1":
        print("Seleccionaste la opcion de registar paciente")
        
        nombre = input("Ingresa el nombre : ")
        ano_nacimiento = int(input("ingresa el año de nacimiento : "))
        peso = float(input("Ingresa el peso : "))
        estatura = float(input("Ingresa la estatura : "))
        direccion = input("Ingresa la direccion : ")
        
        
        paciente = Paciente(nombre =nombre, ano_nacimiento =ano_nacimiento, peso= peso, direccion =direccion, estatura= estatura )
        hospital.registrar_paciente(paciente=paciente)
        print("\nPaciente registrado correctamente")
            
    elif opcion_usuario == "2":
        nombre = input("Ingresa el Nombre")
        ano_nacimiento = int(input("ingresa el año de nacimiento : "))
        rfc = input("Ingresa el rfc : ")
        estatura = float(input("Ingresa la estatura : "))
        direccion = input("Ingresa la direccion : ")
        
        paciente = Paciente(nombre =nombre, ano_nacimiento =ano_nacimiento, peso= peso, direccion =direccion, estatura= estatura )
        hospital.registrar_paciente(paciente=paciente)
        print("\nMedico registrado correctamente")
        
    elif opcion_usuario == "3":
        hospital.mostrar_pacientes()
    
    elif opcion_usuario == "4":
        hospital.mostrar_medicos()
        
    elif opcion_usuario == "5":
        hospital.eliminar_paciente(id)
        
    elif opcion_usuario == "6":
        hospital.eliminar_medico(id)
    
    elif opcion_usuario == "7":
        hospital.mostrar_pacientes_menores_edad
        
    elif opcion_usuario == "8":
        hospital.mostrar_pacientes_mayores_edad
        
    else: 
        print("Hasta Pronto")
        break
        
        
    
        
        
        