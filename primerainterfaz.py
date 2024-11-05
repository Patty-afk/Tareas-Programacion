import tkinter as tk

ventana = tk.Tk()
ventana.title("mi primer interfaz grafica")

etiqueta= tk. Label(ventana,text="hola mundo")
etiqueta.pack(pady=5)

ventana.mainloop()
