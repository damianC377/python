def sistem_par(a):
    if a == int(a) :
        if a > 0 :
            if a % 2 == 0 :
               return("El número digitado es par")
            else:
               return("El número es impar")
        else:
            return("por favor la proxima que se un número positivo")
    else:
        return("Este número no es entero")

num = float(input("Digita un número entero\n"))

print(sistem_par(num))