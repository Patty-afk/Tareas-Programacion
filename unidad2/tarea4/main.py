from tarea4 import coche

#Instancia de la clase persona
coche_1 = coche("Chevrolet", "Aveo", 2012)
coche_1.mostrar_info()
print("Edad del coche:", coche_1.calcular_edad(), "años")

#Segunda Instancia de la clase persona
print("***************")
coche_2 = coche("Nissan", "Sentra", 2006)
coche_2.mostrar_info()
print("Edad del coche:", coche_2.calcular_edad(), "años")

#Segunda Instancia de la clase persona
print("***************")
coche_3 = coche("Honda", "Civic", 2020)
coche_3.mostrar_info()
print("Edad del coche:", coche_3.calcular_edad(), "años")