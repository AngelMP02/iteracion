import tabulate
def separador(cadena):  
    cadena=cadena.split(":")
    lista=[]
    for i in range(0,len(cadena)):
        lista.append(list(cadena[i:i+1]))
        tabla=lista
        encabezado= ["Numero", "Cadena"]
        print(tabulate.tabulate(tabla, encabezado, showindex = True))

separador("Este es un:ejemplo : de cadena a analizar ")


    