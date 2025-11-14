# Autor: Martina Pérez Muñoz
# Fecha: 15/11/2025
# Descripción: Pide un número entero positivo y muestra todos los números desde 1 hasta ese número.
# Entrada esperada: 5
# Salida esperada: 1 2 3 4 5

num = int(input("Introduce un número entero positivo: "))

print("Números desde 1 hasta", num, ":")
for i in range(1, num + 1):
    print(i)
