import sys

sys.path.insert(0,"/Users/smite/Documents/GitHub/iteracion/Ejercicios/ej6")
sys.path.insert(0,"/Users/smite/Documents/GitHub/iteracion/Ejercicios/ej7")
sys.path.insert(0,"/Users/smite/Documents/GitHub/iteracion/Ejercicios/ej8")
sys.path.insert(0,"/Users/smite/Documents/GitHub/iteracion/Ejercicios/ej9")
sys.path.insert(0,"/Users/smite/Documents/GitHub/iteracion/Ejercicios/ej10")
sys.path.insert(0,"/Users/smite/Documents/GitHub/iteracion/Ejercicios/ej11")
sys.path.insert(0,"/Users/smite/Documents/GitHub/iteracion/Ejercicios/ej12")

from ej6 import *
from ej7 import *
from ej8 import *
from ej9 import *
from ej10 import *
from ej11 import *
from ej12 import *

def ejecutar():
    n = input("Inserte el numero de el ejercicio que quieras ejecutar:")

    if n == 6:
        n = 4
        FuncionOrdenar(n,'A','B','C')

    elif n==7:
            
        mat = [[1, 0, 2, -1],
            [3, 0, 0, 5],
            [2, 1, 4, -3],
            [1, 0, 5, 0]]

        print('El determinante de la matriz es:', determinantOfMatrix(mat))


    elif n==8:
        separador("Este es un:ejemplo : de cadena a analizar ")
 

    elif n==9:
        ejecucion4()

    elif n==10:
        ejecucion5()
    elif n==11:
        ejecucion5()
    elif n==12:
        ejecucion5()

    else:
        print("El numero de ejercicio que has insertado es incorrecto!!!!")
ejecutar()