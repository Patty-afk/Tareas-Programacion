from accesorios.accesorios import Accesorios
from accesorios.utilis.tipo import Tipo

class Aretes(Accesorios):
    def __init__(self, nombre, precio, cantidad):
        super().__init__(nombre, precio, cantidad)
        self.tipo =Tipo.ARETES