def sistem_par():
    num = float(input("Digita un número entero\n"))

    if num == int(num) :
        if num > 0 :
            if num % 2 == 0 :
               print("El número digitado es par")
            else:
               print("El número es impar")
        else:
            print("por favor la proxima que se un número positivo")
    else:
        print("Este número no es entero")

sistem_par()