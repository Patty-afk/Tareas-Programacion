class Accesorios:
    nombre: str
    precio: float
    cantidad: int
    
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def calcular_precio_total(self):
        return self.precio * self.cantidad
    
    def mostrar_detalles(self):
        valor_total= self.calcular_precio_total()
        info = f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}, Valor Total :{valor_total}"
        return info
    
