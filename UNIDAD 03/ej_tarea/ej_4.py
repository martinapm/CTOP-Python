# Autor: Martina Pérez Muñoz
# Fecha: 17/11/2025
# Descripción: Calcula el área de un rectángulo tras corregir errores del código original.
# Ejemplo:
# Entrada: base = 5, altura = 3
# Salida: El área es: 15

def area_rectangulo(base, altura):
    area = base * altura
    print("El área es:", area)

# Convertimos la entrada a float
base = float(input("Introduce la base: "))
altura = float(input("Introduce la altura: "))

area_rectangulo(base, altura)
