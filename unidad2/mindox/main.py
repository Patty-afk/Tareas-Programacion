from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from datetime import datetime
from materias.materia import Materia
from grupos.grupo import Grupo


escuela = Escuela()

while True:
    print("**MINDBOX**")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Mostrar estudiantes")
    print("7. Mostrar maestros")
    print("8. mostrar materias")
    print("9. mostrar grupos")
    print("10. eliminar estudiante")
    print("11. eliminar maestro")
    print("12. eliminar materias")
    print ("13. salir")
    
    opcion = input("Ingresa una opcion para continuar: ")
    
    if opcion == "1":
        print("Seleccionaste la opcion para registrar un estudiante")
        
        numero_control = escuela.generar_numero_control()
        print ("Numero de Control: ", numero_control)
        
        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa la curp del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
        fecha_nacimieto = datetime(ano, mes, dia)
        
        estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimieto)
        escuela.registrar_estudiante(estudiante_regis=estudiante)
        
        print("se registro el estudiante correctamente ")
        
        
        
    elif opcion == "2":
        print("\nSeleccionaste la opcion para regitrar un maestro")
        nombre = input("Ingresa el nombre del maestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        rfc = input("Ingresa la rfc del maestro: ")
        sueldo = float(input("Ingresa el sueldo del maestro: "))
        ano_nacimiento = int(input("Ingresa el año de nacimiento del maestro: "))
        numero_control = escuela.generar_numero_control_maestros(año=ano_nacimiento, nombre=nombre, rfc=rfc)
        print("Numero de control: ", numero_control)
        
        maestro = Maestro(numero_control=numero_control, nombre=nombre, apellido=apellido, rfc=rfc, sueldo=sueldo)
        escuela.registrar_maestro(maestro_regis=maestro)
        
        print("se registro el maestro correctamente ")
        
    
    elif opcion == "3":
        print("\nSeleccionaste la opcion de registrar materia")
        nombre_materia=input("ingresa el nombre de la materia: ")
        semestre=int(input("ingresa el semestre: "))
        descripcion=input("ingresa una descripcion: ")
        creditos=int(input("ingresa el creditos: "))
        id_materia= escuela.generar_id_materia(nombre_materia=nombre_materia, semestre=semestre, creditos=creditos)
        print("id de la materia: ",id_materia )
        
        materia = Materia(id_materia=id_materia, nombre_materia=nombre_materia,semestre=semestre, descripcion=descripcion, creditos=creditos)
        escuela.registrar_materia(regis_materia= materia)
     
        print("se registro la materia correctamente :)")
        
     
    elif opcion == "4":
        pass
    
    elif opcion == "5":
        pass
    
    elif opcion == "6":
        escuela.listar_estudiantes()
    
    elif opcion == "7":
        print("maestros registrados")
        escuela.listar_maestros()
    
    elif opcion == "8":
        print("Materias registradas")
        escuela.listar_materias()
    
    elif opcion == "9":
        pass
    
    elif opcion == "10":
        print("seleccionaste la opcion para eliminar un estudiante")

        numero_control= input("ingresa el numero de control del estudiante:")
        
        escuela.eliminar_estudiante(numero_control=numero_control)
        
    
    elif opcion == "11":
        print("seleccionaste la opcion para eliminar un maestro")

        numero_control= input("ingresa el numero de control del maestro:")
        
        escuela.eliminar_maestro(numero_control=numero_control)
        
        
    
    elif opcion == "12":
        print("seleccionaste la opcion para eliminar una materia")

        id_materia= input("ingresa el id de la materia:")
        
        escuela.eliminar_materia(id_materia=id_materia)
        
    elif opcion == "13":
        print("\n Hasta luego")
        break