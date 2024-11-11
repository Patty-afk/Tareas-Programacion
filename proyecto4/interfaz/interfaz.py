import tkinter as tk
from tkinter import messagebox
from accesorios.accesorios import Accesorios
from collares.collares import Collares
from Aretes.aretes import Aretes
from pulseras.pulseras import Pulseras
from Anillos.anillos import Anillos
from excepciones.excepciones import MiError, registrar_producto, escribirnombre, validar_cantidad,validar_precio

class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Registrar Producto")
        self.ventana.geometry("400x400")
        
        self.tipo_producto = tk.StringVar()

        
        label_title = tk.Label(ventana, text="Tiendita Wabi-sabi 🐸", bg="#A8E6CF", fg="white", font=("Arial, 16"))
        label_title.pack(fill=tk.X, pady=10)

        
        tk.Label(ventana, text="Nombre de la joya 💁‍♀️💅:", bg="orange", fg="white", font=("Arial, 12")).pack(pady=10)
        self.entry_nombre = tk.Entry(ventana)
        self.entry_nombre.pack()

        tk.Label(ventana, text="Precio carisimo de paris:", bg="green", fg="white", font=("Arial, 12")).pack(pady=10)
        self.entry_precio = tk.Entry(ventana)
        self.entry_precio.pack()

        tk.Label(ventana, text="Cantidad :", bg="yellow", fg="white", font=("Arial, 12")).pack(pady=10)
        self.entry_cantidad = tk.Entry(ventana)
        self.entry_cantidad.pack()

    
        self.boton_registrar = tk.Button(ventana, text="listo,vamos a registrar", bg="blue", fg="white", font=("Arial, 12"), command=self.registrar_producto, )
        self.boton_registrar.pack(pady=20)

        #aqui personalice errorres
        self.label_resultado = tk.Label(ventana, text="", fg="red", font=("Arial", 15))
        self.label_resultado.pack(pady=10)

    def registrar_producto(self):
        try:
            nombre = self.entry_nombre.get()
            if nombre == "":
                raise MiError("Oye, necesitas poner algo, no dejar en blanco >:v")
            
            precio = float(self.entry_precio.get())
            validar_precio(precio)  

            cantidad = int(self.entry_cantidad.get())
            validar_cantidad(cantidad)  

        
            tipo_producto = "Collares" 

            if tipo_producto == "Collares":
                clase_pro = Collares
            elif tipo_producto == "Aretes":
                clase_pro = Aretes
            elif tipo_producto == "Pulseras":
                clase_pro = Pulseras
            elif tipo_producto == "Anillos":
                clase_pro = Anillos
            else:
                raise MiError("Producto no válido")

            producto = clase_pro(nombre, precio, cantidad)

        
            detalles = producto.mostrar_detalles()
            total = producto.calcular_precio_total()
            self.label_resultado.config(text=f"{detalles}\nValor Total: {total}")

        except MiError as e:
            self.label_resultado.config(text=f"Error: {e}")
        except ValueError:
            self.label_resultado.config(text="Error: Debes ingresar un valor numérico válido para precio y cantidad.")
        

ventana = tk.Tk()
app = Interfaz(ventana)
ventana.mainloop()
