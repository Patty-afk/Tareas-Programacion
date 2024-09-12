class coche:
    marca = ""
    modelo = ""
    año = 0
    
    #MetodoConstructor
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.año = año
        self.modelo = modelo    
    #primermetodo
    def mostrar_info(self):
        print("Marca: ",self.marca)
        print("modelo: ",self.modelo)
        print("año: ",self.año)
        
    def calcular_edad(self):
        año_actual = 2024
        edad = año_actual - self.año
        return edad 
    