class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.chip = True
    
    def tiene_chip(self):
        print(f" {self.chip}")
    
    def hablar(self):
        pass

    def __str__(self):
        return f"{self.nombre}, chip: {self.chip}"
    
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hablar(self):
        print("El perro dice: Guau!")

    def __str__(self):
        return f"{self.nombre}, raza: {self.raza}, chip: {self.chip}"

class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def hablar(self):
        print("El gato dice: Miau, Miau")

    def __str__(self):
        return f"{self.nombre}, color: {self.color}, chip: {self.chip}"
    
perro = Perro("Pepe", "Labrador")
gato = Gato("Gato", "Negro")    