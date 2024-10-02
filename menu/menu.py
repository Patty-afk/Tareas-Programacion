from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from semestres.semestre import Semestre
from datetime import datetime
from carrera.carrera import Carrera
from grupos.grupo import Grupo





class Menu:
    escuela: Escuela = Escuela()
    usuario_estudiante: str ="juan123"
    contrasenia_estudiante: str = "12345*";
    
    usuario_maestro: str ="hilary123"
    contrasenia_maestro: str = "54321*";
    
    
    def login(self):
        intentos =0
        while intentos<5:
        
             print("****** BIENVENIDO **** ")
             print("inicia sesion para continuar")
            
             nombre_usuario = input("ingresa tu nombre de usuario: ")
             contrasenia_usuario =input("ingresa tu contraseña: ")
             
             
             if nombre_usuario == self.usuario_estudiante:
                 if contrasenia_usuario ==self.contrasenia_estudiante:
                     self.mostrar_menu_estudiante()
                     intentos =0
                     
             elif nombre_usuario == self.usuario_maestro:
                if contrasenia_usuario ==self.contrasenia_maestro:
                     self.mostrar_menu_maestro()
                     intentos = 0
            
             else:
                 print("usuario incorrectos, intenta de nuevo")
                 intentos +=1
                
            
             if nombre_usuario== self.usuario and contrasenia_usuario ==self.contrasenia:
                self.mostrar_menu
                
             else:
                print("usuario o contraseña incorrectos. Intenta de nuevo")
                intentos +=1
                
        print("MAXIMOS INTENTOS ALCANZADOS,ADIOS")
        
        
    def mostrar_intento_sesion_fallido(self, intentos_usuario):
        print("usuario incorrectos, intenta de nuevo")
        return intentos_usario +1
        
            
    def mostrar_menu_estudiante(self):
        opcion = 0
        while opcion !=3:
            print("**MINDBOX")
            print("1. Ver horario")
            print("2. ver grupos")
            print("3. salir")
            
            opcion = int(input("Ingresa una opcion "))
            
            if opcion ==3:
                break
    
    def mostrar_menu_maestro(self):
        print("entre al menu del maestro")
        
    
    def mostrar_menu(self):
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
                
                numero_control = self.escuela.generar_numero_control()
                print ("Numero de Control: ", numero_control)
                
                nombre = input("Ingresa el nombre del estudiante: ")
                apellido = input("Ingresa el apellido del estudiante: ")
                curp = input("Ingresa la curp del estudiante: ")
                ano = int(input("Ingresa el año de nacimiento del estudiante: "))
                mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
                dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
                fecha_nacimieto = datetime(ano, mes, dia)
                
                estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimieto)
                self.escuela.registrar_estudiante(estudiante_regis=estudiante)
                
                print("se registro el estudiante correctamente ")
                
                
                
            elif opcion == "2":
                print("\nSeleccionaste la opcion para registrar un maestro")
                nombre = input("Ingresa el nombre del maestro: ")
                apellido = input("Ingresa el apellido del maestro: ")
                rfc = input("Ingresa la rfc del maestro: ")
                sueldo = float(input("Ingresa el sueldo del maestro: "))
                ano_nacimiento = int(input("Ingresa el año de nacimiento del maestro: "))
                numero_control = self.escuela.generar_numero_control_maestros(año=ano_nacimiento, nombre=nombre, rfc=rfc)
                print("Numero de control: ", numero_control)
                
                maestro = Maestro(numero_control=numero_control, nombre=nombre, apellido=apellido, rfc=rfc, sueldo=sueldo)
                self.escuela.registrar_maestro(maestro_regis=maestro)
                
                print("se registro el maestro correctamente ")
                
            
            elif opcion == "3":
                print("\nSeleccionaste la opcion de registrar materia")
                nombre_materia=input("ingresa el nombre de la materia: ")
                semestre=int(input("ingresa el semestre: "))
                descripcion=input("ingresa una descripcion: ")
                creditos=int(input("ingresa el creditos: "))
                id_materia= self.escuela.generar_id_materia(nombre_materia=nombre_materia, semestre=semestre, creditos=creditos)
                print("id de la materia: ",id_materia )
                
                materia = Materia(id_materia=id_materia, nombre_materia=nombre_materia,semestre=semestre, descripcion=descripcion, creditos=creditos)
                self.escuela.registrar_materia(regis_materia= materia)
            
                print("se registro la materia correctamente :)")
                
            
            elif opcion == "4":
                print("\n Seleccionaste la opcion de registrar un nuevo grupo")
                
                tipo = input("ingresa el tipo de grupo(A/B): ")
                id_semestre= input("\n ingresa el id del semestre al que pertenece el grupo: ")
                
                grupo= Grupo(tipo=tipo, id_semestre=id_semestre)
                
                self.escuela.registrar_grupo(grupo=grupo)
                
                print("se registro el grupo correctamente")
                
                
            elif opcion == "5":
                print("\n seleccionaste la opcion de registrar una carrera ")
                
                nombre= input("ingresa el nombre de la carrera: ")
                numero_semestres= input("ingresa el numero de semestres que tendra la carrera: ")
                
                
                carrera = Carrera(nombre=nombre, numero_semestres=numero_semestres)
                
                self.escuela.registrar_carrera(carrera=carrera)
                print("Se registro la carrera correctamente" )
                print("matricula de la carrera: ", carrera.id )
                
                
                
            elif opcion == "6":
                print("\n seleccionaste la opcion de registrar un semestre ")
                
                numero = input("ingresa el numero de semestre: ")
                id_carrera = input("ingresa el id de la carrera: ")
                
                semestre = Semestre(numero=numero, id_carrera=id_carrera)
                
                self.escuela.registrar_semestre(semestre=semestre)
                print("Se registro el semestre correctamente ")
                
                
                
            
            elif opcion == "7":
                pass
            
            elif opcion == "8":
                self.escuela.listar_estudiantes()
            
            elif opcion == "9":
                print("maestros registrados")
                self.escuela.listar_maestros()
            
            elif opcion == "10":
                print("Materias registradas")
                self.escuela.listar_materias()
            
            elif opcion == "11"
                print("Grupos registrados")
                self.escuela.listar_grupos()
            
            
            elif opcion == "12":
                print("Carreras registradas")
                self.escuela.listar_carreras()
            
            elif opcion == "13":
                print("Semestres registrados")
                self.escuela.listar_semestres()  
                
            
            elif opcion == "14":
                print("seleccionaste la opcion para eliminar un estudiante")

                numero_control= input("ingresa el numero de control del estudiante:")
                
                self.escuela.eliminar_estudiante(numero_control=numero_control)
                
            
            elif opcion == "15":
                print("seleccionaste la opcion para eliminar un maestro")

                numero_control= input("ingresa el numero de control del maestro:")
                
                self.escuela.eliminar_maestro(numero_control=numero_control)
                
                
            
            elif opcion == "16":
                print("seleccionaste la opcion para eliminar una materia")

                id_materia= input("ingresa el id de la materia:")
                
                self.escuela.eliminar_materia(id_materia=id_materia)
                

                
            elif opcion == "17":
                print("\n Hasta luego")
                break