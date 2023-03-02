from math import sqrt

numeros = []

rango = int(input("Introduzca el rango de numeros de los que quiere sacar los cuadrados perfectos:"))
cuadrados_perfectos = []

#bucle para añadir los numeros a la lista 
def funcionCuadradosPerfectos(rango):
    n=1
    for i in range(0,rango):
        numeros.append(n)
        n +=1
    print(numeros)

    while rango !=0 :
        rango -= 1

        raiz = sqrt(numeros[rango])

        if int(raiz) == raiz:
            raiz = raiz * raiz #la operacion al cuadrado no me deja hacerla por un error entre float e int
            cuadrados_perfectos.append(raiz)

funcionCuadradosPerfectos(rango)
print(f"Los cuadrados perfectos en el rango de numeros {rango} son {cuadrados_perfectos}")


def sqrt(n):
  if n < 0:
    return
  else:
    return n**0.5
  
print(sqrt(16))
