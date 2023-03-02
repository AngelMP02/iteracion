
try:
    numero=int(input("Introduzca un número:"))
except ValueError:
    print("El input no es un número entero")
try:
    base=int(input("Introduzca una base 2 o mayor:"))
except ValueError:
    print("El input no es un número entero")

