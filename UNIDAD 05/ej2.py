#Atributos protegidos vs Atributos "privados"

class Persona:
    def __init__(self, nombre, edad, dni):
        self._nombre = nombre  # Atributo protegido
        self._edad = edad  # Atributo protegido
        self.__dni = dni     # Atributo "privado"
    
    def get_edad(self):
        """Método getter que retorna la edad de la persona"""
        return self._edad

p = Persona("Ariel", 22, "000000Z")
print(p._nombre) #protegido: técnicamente posible pero no recomendable
print(p._edad)  #protegido: técnicamente posible pero no recomendable
print(p._Persona__dni) #"privado": AttributeError