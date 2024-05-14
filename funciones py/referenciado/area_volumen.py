import math

def area_circulo(a):
    a = math.pi * a**2
    return a

def volumen(a,b):
    return math.pi * a**2*b

radio = float(input("Digita por favor el radio del circulo: "))

altura = float(input("Digita por favor la altura del cilindro: "))
rad = float(input("Digita por favor el radio del cilindro: "))

print("El area del circulo:", area_circulo(radio), "El volumen de cilindro es:", volumen(rad, altura))