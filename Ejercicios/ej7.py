
try:
    numero=int(input("Introduzca un número:"))
except ValueError:
    print("El input no es un número entero")
try:
    base=int(input("Introduzca una base 2 o mayor:"))
except ValueError:
    print("El input no es un número entero")


def transformar(numero, base):
    if base < 2:
        return "La base tiene que ser 2 o mayor"
    elif base >36:
        return numero
    elif numero <= 0:
        print("El numero tiene que ser mayor que 0")
    else:
        conversion = ""
        while numero > 0:
            residuo = numero % base
            if residuo < 10:
                conversion = str(residuo) + conversion
            else:
                conversion = chr(residuo - 10 + ord('A')) + conversion
            numero = numero // base
        print(conversion)

transformar(numero, base)   