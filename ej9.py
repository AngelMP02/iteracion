
diccionario=["avion", "tren", "auto", "camion"]
def tabla(diccionario):
    table=[]
    diccionario.sort()
    for i in range(0,len(diccionario)):
        table.append(diccionario[i:i+1])

    print(table)

tabla(diccionario)