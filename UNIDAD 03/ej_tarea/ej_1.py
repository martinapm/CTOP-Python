# Autor: Martina Pérez Muñoz
# Fecha: 15/11/2025
# Descripción: Solicita tres números enteros al usuario y muestra cuál es el mayor.
# Entrada esperada: 5, 9, 2
# Salida esperada: El número mayor es: 9

# Pedimos los números
n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))
n3 = int(input("Introduce el tercer número: "))

# Comprobamos cuál es el mayor usando condicionales múltiples
if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3

# Mostramos el resultado
print("El número mayor es:", mayor)
