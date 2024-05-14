import math

def mcd(a,b):
    a = int(a)
    b = int(b)
    return math.gcd(a,b)

def mnm(a, b):
    a = int(a)
    b = int(b)
    return (a * b) // mcd(a, b)

num1 = float(input("Digita por favor un número: "))
num2 = float(input("Digita por favor otro número: "))

print("El maximo común divisor de", num1," Y", num2," es:", mcd(num1, num2), "el minimo comun multiplo es:", mnm(num1, num2))