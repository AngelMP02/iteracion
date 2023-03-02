from math import sqrt

numeros = []
n=1
rango = int(input("Introduzca el rango de numeros de los que quiere sacar los cuadrados perfectos:"))
cuadrados_perfectos = []

for i in range(0,rango):
    numeros.append(n)
    n +=1
print(numeros)

while rango !=0 :
    rango -= 1

    raiz = sqrt(numeros[rango])

    if int(raiz) == raiz:
        raiz = raiz * raiz
        cuadrados_perfectos.append(raiz)

print(f"Los cuadrados perfectos en el rango de numeros {rango} son {cuadrados_perfectos}")

   
