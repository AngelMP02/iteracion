import tabulate
diccionario=["avion", "tren", "auto", "camion"]
def tabla(diccionario):
    table=[]
    diccionario.sort()
    for i in range(0,len(diccionario)):
        table.append(diccionario[i:i+1])
    encabezado=["i", "diccionario", "anterior", "siguiente"]
    print(tabulate.tabulate(table, encabezado, showindex = True))


   

tabla(diccionario)