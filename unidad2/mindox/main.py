from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime
from maestros.maestro import Maestro

escuela =Escuela()

while True:
    print("**MINDBOX**")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print ("6. salir")
    
    opcion = input("ingresa una opcion para continuar: ")
    
    if opcion == "1": 
       print("seleccionaste la opcion para registrar un estudiante")
       
       numero_control_estudiante = escuela.generar_numero_control_estudiante()
       print(numero_control_estudiante)
       
       nombre= input ("ingresa el nombre del estudiante: ")
       apellido= input ("ingresa el apellido del estudiante: ")
       curp= input ("ingresa el curp del estudiante: ")
       ano= int(input ("ingresa el año de nacimiento del estudiante: "))
       mes= int(input ("ingresa el mes de nacimiento del estudiante: "))
       dia= int(input ("ingresa el dia de nacimiento del estudiante: "))
       fecha_nacimiento = datetime(ano,mes, dia)
       
    elif opcion == "2": 
        print("seleccionaste la opcion para registrar un maestro")
       
       
        nombre= input ("ingresa el nombre del maestro: ")
        apellido= input ("ingresa el apellido del maestro: ")
        rfc =input("ingresa el rfc de maestro: ")
        sueldo= float(input("ingresa el sueldo del maestro; "))
        ano_nacimiento= int(input ("ingresa el año de nacimiento del Maestro: "))
        mes_nacimiento = int(input("ingresa el mes de nacimiento del maestro: "))
        dia_nacimiento = int(input("ingresa el día de nacimiento del maestro: "))
        fecha_nacimiento_maestro = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
        numero_control_maestro =escuela.generar_numero_control_maestro()
   
        print(numero_control_maestro)
        
        
        
        
        
        
        
    elif opcion == "3": 
       pass 
    elif opcion == "4": 
       pass
    elif opcion == "5": 
       pass 
    elif opcion == "5": 
       pass
    elif opcion == "6":
        print("hasta luego")
        break
    
    
    