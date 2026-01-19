class Saiyan:

    planeta = "Sadala"
    def __init__(self, nombre):
        self.nombre = nombre


class Goku (Saiyan):
    pass

class Vegeta (Saiyan):
    pass

personaje1 = Goku("Goku")
personaje2 = Vegeta("Vegeta")
print(f"{personaje1.nombre} es un Saiyan del planeta {personaje1.planeta}")