# Autor: Martina Pérez Muñoz
# Fecha: 15/11/2025
# Descripción: Compara el tiempo de ejecución entre un bucle for y la función sum().
# Salida esperada: Tiempo de cada método en segundos.

import time

# Versión 1: for
inicio = time.time()

suma = 0
for i in range(1, 1_000_001):
    suma += i

fin = time.time()
print("Tiempo usando for:", fin - inicio, "segundos")

# Versión 2: sum(range())
inicio = time.time()

suma2 = sum(range(1, 1_000_001))

fin = time.time()
print("Tiempo usando sum(range()):", fin - inicio, "segundos")
