import math

def mcd():
    num1 = int(input("Digita por favor un número entero: "))
    num2 = int(input("Digita por favor otro número entero: "))
    return math.gcd(num1,num2)
def mcm():
    num1 = int(input("Digita por favor un número entero: "))
    num2 = int(input("Digita por favor otro número entero: "))
    return (num1 * num2) // math.gcd(num1,num2)

print("El numero mazimo comun divisor es:",mcd())
print("El minimo comun multiplo es:", mcm())