class Circulo:
    radio = 0
    
    def __init__(self,radio):
       self.radio = radio
       
       
    def calcula_perimetro(self):
           perimetro =  2 * 3.141516 * self.radio
           print ("el perimetro del circulo:", perimetro)
           
           
    def calcular_area(self):
        area = 3.141516 * (self.radio **2)
        print("el area del circulo es:", area) 