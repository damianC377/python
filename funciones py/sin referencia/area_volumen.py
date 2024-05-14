def area_circulo():
    pi = 3.14159
    radio = float(input("Por favor digita el radio: "))
    return pi * radio**2

def cilindro():
    pi = 3.14159
    altura = float(input("Digita por favor la altura: "))
    radio = float(input("Digita por favor el radio del cilindro: "))
    return pi * radio**2 * altura


area = area_circulo()
volumen = cilindro()
print("el radio de el circulo es:", area, "El volumen del cilindro es:", volumen)