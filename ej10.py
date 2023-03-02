class Persona:
    def __init__(self, identidad, edad, padre, madre):
        self.identidad = identidad
        self.edad = edad
        self.padre = padre
        self.madre = madre
familias = [None] * 1000 #creo una lista con 1000 elementos

personas_entre_20_30 = []
def personas_20_30():
        for persona in familias:
            if persona is not None and 20 <= persona.edad <= 30:
                personas_20_30.append(persona)


