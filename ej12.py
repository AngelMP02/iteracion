from math import sqrt

numeros = []
n=1
rango = int(input("Introduzca el rango de numeros de los que quiere sacar los cuadrados perfectos:"))
for i in range(0,rango):
    numeros.append(n)
    n +=1
print(numeros)

while rango !=0 :
    rango -= 1
    raiz = sqrt(numeros(rango))
    print(raiz)
