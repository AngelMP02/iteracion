import tabulate
def tabla(diccionario):
    table=[]
    for i in range(0,len(diccionario)):
        table.append(diccionario[i:i+1])
    encabezado=["i", "diccionario", "anterior", "siguiente"]
    print(tabulate.tabulate(table, encabezado, showindex = True))

tabla(diccionario=["avion", "tren", "auto", "camion"])


   

