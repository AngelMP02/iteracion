class PERSONA:
    def __init__(self, id_persona, nombre, apellido, edad, id_padre, id_madre):
     self.id_persona = id_persona
     self.nombre = nombre
     self.apellido = apellido
     self.edad = edad
     self.id_padre = id_padre
     self.id_madre = id_madre


familias = [None] * 1000

familias = [None] * 1000 #creo una lista con 1000 elementos

personas_entre_20_30 = []
def personas_20_30():
        for persona in familias:
            if persona is not None and 20 <= persona.edad <= 30:
                personas_entre_20_30.append(persona)
huérfanos_menos_15 = []
def numero_huerfanos_menor_15():
     




