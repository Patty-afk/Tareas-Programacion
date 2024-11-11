class MiError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


def registrar_producto(tipo_product):
    if tipo_product not in ["Collares", "Aretes", "Pulseras", "Anillos"]:
        raise MiError("Diosito no autorizo este tipo de producto")
    else:
        print(f"Registrando producto de tipo {tipo_product}...") 

def escribirnombre(nombre):
    if nombre == "":
        raise MiError("No se puede imprimir, el nombre está vacío.")
    else:
        print(f"El nombre es: {nombre}")


def validar_precio(precio):
    if precio < 0:
        raise MiError("como que precio negativo?, yo no te debo nada >:v")
    else:
        print(f"Precio registrado: {precio}.")
        
        
def validar_cantidad(cantidad):
    if cantidad < 0:
        raise MiError("La cantidad no puede ser negativa, no me vas a robar productos")
    else:
        print(f"Cantidad registrada: {cantidad}.")