try:
    a = int(input("Introduzca un numero entero:"))
    b = int(input("Introduzca un numero entero:"))
except ValueError:
    print("El numero que has introducio no es un numero entero")

def mcd(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
        #la variable temporal se usa para cambiar los valore de a y b
    return a

resultado = mcd(a, b)
print(f"El Máximo común divisor de {a} y {b} es {resultado}")
