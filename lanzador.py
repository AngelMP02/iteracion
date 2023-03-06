import sys

sys.path.insert(0,"/Users/smite/Documents/GitHub/iteracion/Ejercicios")
# sys.path.insert(0,"/Users/smite/Documents/GitHub/iteracion/Ejercicios/ej7")
# sys.path.insert(0,"/Users/smite/Documents/GitHub/iteracion/Ejercicios/ej8")
# sys.path.insert(0,"/Users/smite/Documents/GitHub/iteracion/Ejercicios/ej9")
# sys.path.insert(0,"/Users/smite/Documents/GitHub/iteracion/Ejercicios/ej10")
# sys.path.insert(0,"/Users/smite/Documents/GitHub/iteracion/Ejercicios/ej11")
# sys.path.insert(0,"/Users/smite/Documents/GitHub/iteracion/Ejercicios/ej12")

from Ejercicios import ej6
from Ejercicios import ej7
from Ejercicios import ej8
from Ejercicios import ej9
from Ejercicios import ej10
from Ejercicios import ej11
from Ejercicios import ej12

# from ej6 import *
# from ej7 import *
# from ej8 import *
# from ej9 import *
# from ej10 import *
# from ej11 import *
# from ej12 import *

def ejecutar():
    n = input("Inserte el numero de el ejercicio que quieras ejecutar:")

    if n == 6:
        return #


    elif n==7:
        try:
            numero=int(input("Introduzca un número:"))
        except ValueError:
            print("El input no es un número entero")
        try:
            base=int(input("Introduzca una base 2 o mayor:"))
        except ValueError:
            print("El input no es un número entero")

        transformar(numero, base)  


    elif n==8:
        separador("Este es un:ejemplo : de cadena a analizar ")
 

    elif n==9:
        diccionario=["avion", "tren", "auto", "camion"]
        print("Tabla incial:")
        tabla(diccionario)

        print("\n Tabla ordenada:")
        diccionario.sort()
        tabla(diccionario)

    elif n==10:
        return

    elif n==11:
        try:
            a = int(input("Introduzca un numero entero:"))
            b = int(input("Introduzca un numero entero:"))
        except ValueError:
            print("El numero que has introducio no es un numero entero")
        resultado = mcd(a, b)
        print(f"El Máximo común divisor de {a} y {b} es {resultado}")

    elif n==12:
        numeros = []

        rango = int(input("Introduzca el rango de numeros de los que quiere sacar los cuadrados perfectos:"))
        cuadrados_perfectos = []
        funcionCuadradosPerfectos(rango)
        print(f"Los cuadrados perfectos en el rango de numeros {rango} son {cuadrados_perfectos}")

        print(sqrt(16))

    else:
        print("El numero de ejercicio que has insertado es incorrecto!!!!")

ejecutar()