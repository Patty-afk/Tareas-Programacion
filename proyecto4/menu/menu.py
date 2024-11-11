from excepciones.excepciones import MiError, registrar_producto, escribirnombre, validar_precio, validar_cantidad
from accesorios.accesorios import Accesorios
from collares.collares import Collares
from Aretes.aretes import Aretes
from pulseras.pulseras import Pulseras
from Anillos.anillos import Anillos

class Menu:
    def __init__(self):
        self.productos = {
            "Collares": [],
            "Aretes": [],
            "Pulseras": [],
            "Anillos": []
        } 

    def mostrar_menu(self):
        while True:
            print("\nMenu accesorios 🙆‍♀️")
            print("1. Registrar Collares")
            print("2. Registrar Aretes")
            print("3. Registrar Pulseras")
            print("4. Registrar Anillos")
            print("5. Ver Inventario de Collares")
            print("6. Ver Inventario de Aretes")
            print("7. Ver Inventario de Pulseras")
            print("8. Ver Inventario de Anillos")
            print("9. Ver Inventario Total")
            print("10. Salir")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.registrar_producto("Collares")
            elif opcion == "2":
                self.registrar_producto("Aretes")
            elif opcion == "3":
                self.registrar_producto("Pulseras")
            elif opcion == "4":
                self.registrar_producto("Anillos")
            elif opcion == "5":
                self.ver_inv("Collares")
            elif opcion == "6":
                self.ver_inv("Aretes")
            elif opcion == "7":
                self.ver_inv("Pulseras")
            elif opcion == "8":
                self.ver_inv("Anillos")
            elif opcion == "9":
                self.inv_total()
            elif opcion == "10":
                print("ADIOS")
                break
            else:
                print("Esa no era una opcion 🤦‍♀️")

    def registrar_producto(self, tipo_product):
        try:
            if tipo_product == "Collares":
                clase_pro = Collares
            elif tipo_product == "Aretes":
                clase_pro = Aretes
            elif tipo_product == "Pulseras":
                clase_pro = Pulseras
            elif tipo_product == "Anillos":
                clase_pro = Anillos
            else:
                raise MiError("Diosito no autorizo este producto ")

            
            nombre = input(f"nombre de {tipo_product}: ")
            if nombre == "":
                raise MiError("Oye tu, necesitas poner algo, no dejar en blanco >:v")
            
            
            precio = float(input(f"precio de {tipo_product}: "))
            validar_precio(precio)  

            
            cantidad = int(input(f"cantidad de {tipo_product}: "))
            validar_cantidad(cantidad)  

            
            producto = clase_pro(nombre, precio, cantidad)
            self.productos[tipo_product].append(producto)
            print(f"{tipo_product} registrado :D")

        except MiError as e:
            print(f"Error: {e}")
        except ValueError:
            print("Error: Debes ingresar un valor numérico válido para precio y cantidad.")
        
    def ver_inv(self, tipo_product):
        inventario = self.productos[tipo_product]
        if len(inventario) == 0:
            print(f"No hay {tipo_product} registrados :c")
        else:
            for producto in inventario:
                print(producto.mostrar_detalles())
                print(f"Valor total de inventario 💅 {producto.calcular_precio_total()}")

    def inv_total(self):
        if all(len(inventario) == 0 for inventario in self.productos.values()):
            print("No hay productos ")
        else:
            for tipo_product, inventario in self.productos.items():
                if len(inventario) > 0:
                    print(f"\nInventario de {tipo_product}:")
                    for producto in inventario:
                        print(producto.mostrar_detalles())
                        print(f"Valor total de inventario: {producto.calcular_precio_total()}")
