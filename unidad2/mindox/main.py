from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from datetime import datetime
from materias.materia import Materia
from grupos.grupo import Grupo
from carrera.carrera import Carrera
from semestres.semestre import Semestre


escuela = Escuela()

while True:
    print("**MINDBOX**")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print ("5. Registrar carrera")
    print ("6. Registrar semestre")
    print("7. Registrar horario")
    print("8. Mostrar estudiantes")
    print("9. Mostrar maestros")
    print("10. mostrar materias")
    print("11. mostrar grupos")
    print("12. mostrar carreras")
    print("13. mostrar semestres")
    print("14. eliminar estudiante")
    print("15. eliminar maestro")
    print("16. eliminar materias")
    print ("17. salir")
    
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
        print("\nSeleccionaste la opcion para registrar un maestro")
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
        print("\n Seleccionaste la opcion de registrar un nuevo grupo")
        
        tipo = input("ingresa el tipo de grupo(A/B): ")
        id_semestre= input("\n ingresa el id del semestre al que pertenece el grupo: ")
        
        grupo= Grupo(tipo=tipo, id_semestre=id_semestre)
        
        escuela.registrar_grupo(grupo=grupo)
        
        print("se registro el grupo correctamente")
        
        
    elif opcion == "5":
        print("\n seleccionaste la opcion de registrar una carrera ")
        
        nombre= input("ingresa el nombre de la carrera: ")
        numero_semestres= input("ingresa el numero de semestres que tendra la carrera: ")
        
        
        carrera = Carrera(nombre=nombre, numero_semestres=numero_semestres)
        
        escuela.registrar_carrera(carrera=carrera)
        print("Se registro la carrera correctamente" )
        print("matricula de la carrera: ", carrera.id )
        
        
        
    elif opcion == "6":
        print("\n seleccionaste la opcion de registrar un semestre ")
        
        numero = input("ingresa el numero de semestre: ")
        id_carrera = input("ingresa el id de la carrera: ")
        
        semestre = Semestre(numero=numero, id_carrera=id_carrera)
        
        escuela.registrar_semestre(semestre=semestre)
        print("Se registro el semestre correctamente ")
        
        
        
    
    elif opcion == "7":
        pass
    
    elif opcion == "8":
        escuela.listar_estudiantes()
    
    elif opcion == "9":
        print("maestros registrados")
        escuela.listar_maestros()
    
    elif opcion == "10":
        print("Materias registradas")
        escuela.listar_materias()
    
    elif opcion == "11":
        print("Grupos registrados")
        escuela.listar_grupos()
    
    
    elif opcion == "12":
        print("Carreras registradas")
        escuela.listar_carreras()
    
    elif opcion == "13":
        print("Semestres registrados")
        escuela.listar_semestres()  
        
    
    elif opcion == "14":
        print("seleccionaste la opcion para eliminar un estudiante")

        numero_control= input("ingresa el numero de control del estudiante:")
        
        escuela.eliminar_estudiante(numero_control=numero_control)
        
    
    elif opcion == "15":
        print("seleccionaste la opcion para eliminar un maestro")

        numero_control= input("ingresa el numero de control del maestro:")
        
        escuela.eliminar_maestro(numero_control=numero_control)
        
        
    
    elif opcion == "16":
        print("seleccionaste la opcion para eliminar una materia")

        id_materia= input("ingresa el id de la materia:")
        
        escuela.eliminar_materia(id_materia=id_materia)
        

        
    elif opcion == "17":
        print("\n Hasta luego")
        break